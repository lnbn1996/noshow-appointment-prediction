"""Phan tich du lieu no-show (Kaggle, CC BY-NC-SA 4.0) -> hinh PNG + ket_qua.json cho bai YC1/YC2."""
import json, zipfile, pathlib
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             roc_auc_score, roc_curve, confusion_matrix, ConfusionMatrixDisplay)

here = pathlib.Path(__file__).resolve().parent
zp = here.parent / "data" / "KaggleV2-May-2016.csv.zip"
import sys
POSTER = "--poster" in sys.argv  # python phan_tich_noshow.py --poster -> hinh_poster/ (chu to, 400 dpi)
DPI = 400 if POSTER else 200
out = here.parent / "results" / ("poster" if POSTER else ""); out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.size": 15 if POSTER else 11, "axes.spines.top": False, "axes.spines.right": False})
C = {"No": "#4C78A8", "Yes": "#E45756"}

df = pd.read_csv(zipfile.ZipFile(zp).open("KaggleV2-May-2016.csv"))
n0 = len(df)
df["lead_days"] = (pd.to_datetime(df.AppointmentDay).dt.normalize()
                   - pd.to_datetime(df.ScheduledDay).dt.normalize()).dt.days
bad_age = int((df.Age < 0).sum()); bad_lead = int((df.lead_days < 0).sum())
df = df[(df.Age >= 0) & (df.lead_days >= 0)].copy()
df["y"] = (df["No-show"] == "Yes").astype(int)
df["female"] = (df.Gender == "F").astype(int)
df["weekday"] = pd.to_datetime(df.AppointmentDay).dt.dayofweek
df["Handcap"] = (df.Handcap > 0).astype(int)
feats = ["Age", "lead_days", "weekday", "female", "Scholarship", "Hipertension",
         "Diabetes", "Alcoholism", "Handcap", "SMS_received"]
X, y = df[feats], df.y
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, class_weight="balanced")),
    "Decision Tree": DecisionTreeClassifier(max_depth=6, class_weight="balanced", random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_leaf=20,
                                            class_weight="balanced", n_jobs=-1, random_state=42),
}
res, probs, preds = {}, {}, {}
for k, m in models.items():
    m.fit(Xtr, ytr); p = m.predict_proba(Xte)[:, 1]; yh = (p >= 0.5).astype(int)
    probs[k], preds[k] = p, yh
    res[k] = dict(accuracy=accuracy_score(yte, yh), precision=precision_score(yte, yh),
                  recall=recall_score(yte, yh), f1=f1_score(yte, yh), auc=roc_auc_score(yte, p))

# --- hinh a: phan bo lop
fig, ax = plt.subplots(figsize=(4.2, 3.4))
vc = df["No-show"].value_counts()
ax.bar(["Đến khám", "Vắng mặt"], [vc["No"], vc["Yes"]], color=[C["No"], C["Yes"]])
for i, v in enumerate([vc["No"], vc["Yes"]]): ax.text(i, v, f"{v:,}\n({v/len(df):.1%})".replace(",", "."), ha="center", va="bottom")
ax.set_ylabel("Số lượt hẹn"); ax.set_ylim(0, vc.max() * 1.2); fig.tight_layout(); fig.savefig(out / "fig_phanbo.png", dpi=DPI); plt.close(fig)

# --- hinh b: ty le vang theo so ngay dat truoc
bins = [-1, 0, 3, 7, 14, 30, 60, 200]; lab = ["0", "1–3", "4–7", "8–14", "15–30", "31–60", ">60"]
df["lead_bin"] = pd.cut(df.lead_days, bins=bins, labels=lab)
rate = df.groupby("lead_bin", observed=True).y.agg(["mean", "size"])
fig, ax = plt.subplots(figsize=(4.2, 3.4))
ax.bar(lab, rate["mean"] * 100, color=C["Yes"]); ax.axhline(df.y.mean() * 100, color="k", ls="--", lw=1)
ax.set_xlabel("Số ngày đặt trước" if POSTER else "Số ngày từ lúc đặt lịch đến ngày khám"); ax.set_ylabel("Tỷ lệ vắng mặt (%)")
plt.setp(ax.get_xticklabels(), rotation=(45 if POSTER else 30), ha="right", rotation_mode="anchor"); fig.tight_layout(); fig.savefig(out / "fig_leadtime.png", dpi=DPI); plt.close(fig)

# --- hinh c: ma tran nham lan RF
fig, ax = plt.subplots(figsize=(4.2, 3.4))
ConfusionMatrixDisplay(confusion_matrix(yte, preds["Random Forest"]), display_labels=["Đến", "Vắng"]).plot(ax=ax, cmap="Blues", colorbar=False, values_format="d")
ax.set_xlabel("Dự đoán"); ax.set_ylabel("Thực tế"); fig.tight_layout(); fig.savefig(out / "fig_confusion.png", dpi=DPI); plt.close(fig)
cm = confusion_matrix(yte, preds["Random Forest"]).tolist()

# --- hinh d: ROC
fig, ax = plt.subplots(figsize=(4.2, 3.4))
for k, col in zip(models, ["#4C78A8", "#F58518", "#54A24B"]):
    fpr, tpr, _ = roc_curve(yte, probs[k]); ax.plot(fpr, tpr, color=col, label=f"{k} ({res[k]['auc']:.3f})")
ax.plot([0, 1], [0, 1], "k:", lw=1); ax.set_xlabel("Tỷ lệ dương tính giả"); ax.set_ylabel("Tỷ lệ dương tính thật")
ax.legend(fontsize=(12 if POSTER else 8), loc="lower right"); fig.tight_layout(); fig.savefig(out / "fig_roc.png", dpi=DPI); plt.close(fig)

# --- hinh e: do quan trong cua bien (RF)
imp = pd.Series(models["Random Forest"].feature_importances_, index=feats).sort_values()
names = {"Age": "Tuổi", "lead_days": "Số ngày đặt trước", "weekday": "Thứ trong tuần", "female": "Giới nữ", "Scholarship": "Học bổng (Bolsa Família)",
         "Hipertension": "Tăng huyết áp", "Diabetes": "Tiểu đường", "Alcoholism": "Nghiện rượu", "Handcap": "Khuyết tật", "SMS_received": "Nhận SMS"}
fig, ax = plt.subplots(figsize=(6, 3.6)); ax.barh([names[i] for i in imp.index], imp.values, color="#4C78A8")
ax.set_xlabel("Độ quan trọng (Gini)"); fig.tight_layout(); fig.savefig(out / "fig_importance.png", dpi=DPI); plt.close(fig)

# --- thong ke bo sung
sms = df.groupby("SMS_received").y.mean().to_dict()
info = dict(n_raw=n0, n_clean=len(df), removed_age=bad_age, removed_lead=bad_lead, n_train=len(Xtr), n_test=len(Xte),
            noshow_rate=df.y.mean(), n_patients=int(df.PatientId.nunique()), sms_rate=sms,
            lead_rate={str(k): float(v) for k, v in rate["mean"].items()},
            lead_mean_yes=float(df[df.y == 1].lead_days.mean()), lead_mean_no=float(df[df.y == 0].lead_days.mean()),
            importance=imp.sort_values(ascending=False).to_dict(), cm_rf=cm, results=res)
if not POSTER: (here.parent / "results" / "ket_qua.json").write_text(json.dumps(info, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print(json.dumps(info, ensure_ascii=False, indent=1, default=float))
