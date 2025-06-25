# Label Feasibility Dashboard (Smoothed)

This interactive Streamlit app evaluates if label sizes can reach full speed within ramp time based on system parameters.

## ✅ Features

- 📈 **Smoothed Line Chart**: Minimum label size required per speed using cubic spline interpolation.
- 🔥 **Heatmap**: Visual matrix of label size vs speed feasibility.
- 📦 All data is embedded, no external files needed.

## ⚙️ Parameters
- Roller diameter: 54 mm
- Gear ratio: 2.4545...
- Steps per rev: 200 × 16 (microstepping)
- Max speed: 40 m/min
- Max ramp time: 80 ms

## 🚀 Setup

1. Clone this repo or upload files to your own GitHub repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Run Locally

```bash
streamlit run label_feasibility_smoothed.py
```

## 🌐 Deploy on Streamlit Cloud

1. Upload this repo to GitHub.
2. Visit [Streamlit Cloud](https://streamlit.io/cloud) and deploy using your GitHub repo.

---

Built with ❤️ using Streamlit, Plotly, and SciPy.
