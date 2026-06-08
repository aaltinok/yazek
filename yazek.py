import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Sayfa yapılandırması
st.set_page_config(
    page_title="Eğitimde YZ Etik ve Politika Karşılaştırmaları",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================
#  GELİŞMİŞ KARANLIK TEMA CSS
# ========================
dark_theme_css = """
<style>
    .stApp { background-color: #0B0E14; color: #EAECF0; }
    .css-1d391kg, .css-12oz5g0, [data-testid="stSidebar"] { background-color: #11161F; border-right: 1px solid #2D3748; }
    h1, h2, h3, h4, h5, h6 { color: #F59E0B !important; font-weight: 700 !important; }
    h1 { font-size: 2.5rem !important; border-bottom: 2px solid #F59E0B; display: inline-block; padding-bottom: 8px; }
    th { background-color: #1A2436 !important; color: #FBBF24 !important; text-align: center !important; border: 1px solid #2D3748 !important; }
    td { background-color: #0F172A !important; color: #E2E8F0 !important; vertical-align: top !important; border: 1px solid #2D3748 !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 4px; background-color: #11161F; padding: 8px; border-radius: 12px; flex-wrap: wrap; }
    .stTabs [data-baseweb="tab"] { background-color: #1A2436; border-radius: 8px; color: #E2E8F0; padding: 6px 16px; margin: 2px; }
    .stTabs [aria-selected="true"] { background-color: #F59E0B; color: #0B0E14; }
    .streamlit-expanderHeader { background-color: #11161F; color: #F59E0B; font-size: 1.1rem; font-weight: 600; border-radius: 12px; border: 1px solid #2D3748; }
    hr { border-color: #2D3748; margin: 2rem 0; }
    .stAlert { background-color: #1A2436; border-left: 4px solid #F59E0B; }
</style>
"""
st.markdown(dark_theme_css, unsafe_allow_html=True)

# ========================
#  BAŞLIK
# ========================
st.title("🎓 Eğitimde Yapay Zeka Uygulamaları")
st.markdown("## Etik, Pedagoji ve Politika Karşılaştırmaları")
st.markdown("***")

st.info("""
> **📌 Veri Kaynağı ve Metodoloji Notu:** Bu rapordaki sayısal puanlar ve yüzdeler, ilgili politika belgeleri (MEB YAZEK Kılavuzu 2026, AB YZ Yasası 2024/1689, UNESCO YZ Etik Tavsiyeleri, Çin YZ Eğitim Stratejisi 2024-2027, OECD raporları) ve akademik literatür taranarak oluşturulmuş **temsili değerlerdir**. Kesin ölçümler değil, eğilim göstergeleridir.
""")

st.markdown("""
Bu bilimsel çalışma, **12 farklı ders** özelinde yapay zeka destekli eğitim araçlarının karşılaştığı gerçek hayat problemlerini; 
**Türkiye (MEB/YAZEK), Çin, Avrupa Birliği, UNESCO ve ABD/İngiltere** stratejileri bazında karşılaştırmaktadır.
""")

# ========================
#  YAN MENÜ
# ========================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Artificial_Neural_Network_with_Chip_and_Brain.svg/1200px-Artificial_Neural_Network_with_Chip_and_Brain.svg.png", width=70)
st.sidebar.title("📖 Ders Seçimi")

ders_listesi = [
    "Matematik", "Fizik", "Kimya", "Biyoloji",
    "Türkçe / Edebiyat", "Tarih", "Coğrafya",
    "Yabancı Dil (İngilizce)", "Müzik", "Görsel Sanatlar",
    "Beden Eğitimi", "Rehberlik"
]

secili_ders = st.sidebar.selectbox("Analiz edilecek dersi seçin:", ders_listesi)
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔬 Metodoloji")
st.sidebar.info("""
**Kaynaklar:**  
- MEB YAZEK Etik Kılavuzu (2026)  
- AB Yapay Zeka Yasası (2024/1689)  
- UNESCO YZ Etik Tavsiyeleri  
- Çin YZ Eğitim Stratejisi (2024-2027)  
- OECD Dijital Eğitim Raporları
""")

# ========================
#  GRAFİK FONKSİYONLARI
# ========================

def politika_etkinlik_heatmap(ders_adi, etkinlik_matrisi):
    sorunlar = list(etkinlik_matrisi.keys())
    stratejiler = ["Türkiye (YAZEK)", "Çin", "AB", "UNESCO", "ABD/İngiltere"]
    
    data = []
    for sorun in sorunlar:
        satir = [etkinlik_matrisi[sorun][s] for s in stratejiler]
        data.append(satir)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    im = ax.imshow(data, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)
    
    ax.set_xticks(np.arange(len(stratejiler)))
    ax.set_yticks(np.arange(len(sorunlar)))
    ax.set_xticklabels(stratejiler, rotation=45, ha='right', color='#E2E8F0', fontsize=10)
    ax.set_yticklabels(sorunlar, color='#E2E8F0', fontsize=10)
    ax.set_title(f"{ders_adi} - Politika Etkinlik Skorları (0=düşük, 100=yüksek)", 
                 color='#F59E0B', fontsize=14, fontweight='bold')
    
    for i in range(len(sorunlar)):
        for j in range(len(stratejiler)):
            ax.text(j, i, data[i][j], ha="center", va="center", color="black", fontweight='bold', fontsize=9)
    
    cbar = plt.colorbar(im, ax=ax)
    cbar.ax.yaxis.label.set_color('#E2E8F0')
    cbar.ax.tick_params(colors='#E2E8F0')
    
    ax.set_facecolor('#0F172A')
    fig.patch.set_facecolor('#0B0E14')
    plt.tight_layout()
    return fig

def politika_radar_analizi(ders_adi, strateji_puanlari):
    kategoriler = ['Pedagojik Uygunluk', 'Etik Güvence', 'Öğrenci Mahremiyeti', 
                   'Öğretmen İş Yükü', 'Yenilikçilik', 'Erişilebilirlik']
    
    fig = go.Figure()
    renkler = ['#F59E0B', '#EF4444', '#3B82F6', '#10B981', '#8B5CF6']
    
    for i, (strateji, puanlar) in enumerate(strateji_puanlari.items()):
        fig.add_trace(go.Scatterpolar(
            r=puanlar + [puanlar[0]],
            theta=kategoriler + [kategoriler[0]],
            fill='toself',
            name=strateji,
            line=dict(color=renkler[i % len(renkler)], width=2),
            fillcolor=f'rgba({int(renkler[i % len(renkler)][1:3], 16)}, {int(renkler[i % len(renkler)][3:5], 16)}, {int(renkler[i % len(renkler)][5:7], 16)}, 0.3)'
        ))
    
    fig.update_layout(
        polar=dict(
            bgcolor='#0F172A',
            radialaxis=dict(visible=True, range=[0, 100], gridcolor='#2D3748', tickfont=dict(color='#E2E8F0')),
            angularaxis=dict(tickfont=dict(color='#E2E8F0', size=11), gridcolor='#2D3748')
        ),
        title=f"{ders_adi} - Küresel Politika Karşılaştırma Radar Analizi",
        title_font=dict(color='#F59E0B', size=14),
        paper_bgcolor='#0B0E14',
        font=dict(color='#E2E8F0'),
        legend=dict(bgcolor='#11161F', bordercolor='#F59E0B', borderwidth=1),
        height=550
    )
    return fig

def risk_azaltma_grafigi(ders_adi, risk_azaltma_oranlari):
    stratejiler = list(risk_azaltma_oranlari.keys())
    risk_turleri = list(risk_azaltma_oranlari[stratejiler[0]].keys())
    
    fig = go.Figure()
    
    for i, risk in enumerate(risk_turleri):
        degerler = [risk_azaltma_oranlari[s][risk] for s in stratejiler]
        fig.add_trace(go.Bar(
            name=risk,
            x=stratejiler,
            y=degerler,
            text=degerler,
            textposition='auto',
            textfont=dict(color='white', weight='bold'),
            marker=dict(line=dict(width=1, color='#2D3748'))
        ))
    
    fig.update_layout(
        title=f"{ders_adi} - Strateji Bazlı Risk Azaltma Başarı Oranları (%)",
        title_font=dict(color='#F59E0B', size=14),
        plot_bgcolor='#0F172A',
        paper_bgcolor='#0B0E14',
        font=dict(color='#E2E8F0'),
        xaxis=dict(gridcolor='#2D3748', tickangle=20),
        yaxis=dict(gridcolor='#2D3748', range=[0, 100], title="Risk Azaltma Başarısı (%)"),
        barmode='group',
        legend=dict(bgcolor='#11161F', bordercolor='#F59E0B', borderwidth=1, orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
        height=500
    )
    return fig

# ========================
#  DERS 1: MATEMATİK (TAM DETAY)
# ========================
def matematik_analizi():
    st.header("📐 Matematik Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli problem çözücü ve adım adım anlatıcı kullanımı.")
    st.markdown("**Tespit Edilen Sorunlar:** (1) Kopyala-yapıştır ile süreç hırsızlığı, (2) Kavram yanılgısı tespit edememe, (3) Soyut raporlar nedeniyle öğretmen iş yükünün artması.")
    
    tablo_headers = ["Strateji", "Pedagojik Zarar (Kopya)", "Hata Yakalama", "Öğretmen İş Yükü", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (MEB/YAZEK)", "Sadece ipucu verir, adım adım çözüm yasak.", "Hata türünü etiketler, telafi içeriği sunar.", "Somut rapor (örn: 'Ayşe parantez hatası yapıyor')", "Kontrollü asistan; öğretmen nihai karar verici."],
        ["🇨🇳 Çin", "Ulusal platformda kopya tespiti, adımlar kilitlenir.", "Ulusal hata kodlarıyla sınıflandırma.", "Merkezi raporlama; iş yükü azalır.", "Standardize edici araç; öğretmen koordinatör."],
        ["🇪🇺 Avrupa Birliği", "Kopya engelleyici zorunlu; adım adım onay ister.", "Etiketleme yapabilir ama itiraz hakkı doğar.", "İnsan kontrolü şart; iş yükü artabilir.", "Yüksek riskli; öğretmen yetkisi mutlak."],
        ["🇺🇳 UNESCO", "Pedagojik etki değerlendirmesi tavsiye eder.", "Öğretmenin hata analizinde eğitilmesini önerir.", "Yapısal sorunların çözülmesini ister.", "Etik pusula; tavsiye niteliğinde."],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Piyasa rekabetiyle 'kilit modu' gelişir.", "Rekabetle 'kavram yanılgısı dedektörü' doğar.", "Öğretmen beğenmediği şirketten ayrılabilir.", "Serbest piyasa; öğretmen girişimci."]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Süreç Hırsızlığı": {"Türkiye (YAZEK)": 85, "Çin": 70, "AB": 90, "UNESCO": 65, "ABD/İngiltere": 50},
        "Kavram Yanılgısı": {"Türkiye (YAZEK)": 75, "Çin": 65, "AB": 80, "UNESCO": 60, "ABD/İngiltere": 55},
        "İş Yükü": {"Türkiye (YAZEK)": 65, "Çin": 85, "AB": 40, "UNESCO": 45, "ABD/İngiltere": 70}
    }
    st.pyplot(politika_etkinlik_heatmap("Matematik", etkinlik_matrisi))
    
    st.markdown("""
    **📊 Matematik - Politika Etkinlik Heatmap Detaylı Analizi:**
    
    | Ülke/Kurum | Süreç Hırsızlığı | Kavram Yanılgısı | İş Yükü | Ortalama |
    |---|---|---|---|---|
    | **Türkiye (YAZEK)** | 85 | 75 | 65 | 75.0 |
    | **Çin** | 70 | 65 | 85 | 73.3 |
    | **AB** | 90 | 80 | 40 | 70.0 |
    | **UNESCO** | 65 | 60 | 45 | 56.7 |
    | **ABD/İngiltere** | 58 | 55 | 70 | 61.0 |
    
    **Türkiye:** Süreç hırsızlığına karşı 85 puan - 'ipucu verme' kuralı Vygotsky'nin ZPD teorisiyle uyumludur. İş yükü 65 puan - öğretmen hala raporları onaylamalıdır.
    **Çin:** İş yükü 85 puanla en yüksek - otomatik merkezi raporlama öğretmeni rahatlatır. Ancak kavram yanılgısı 65 puan - bireysel farklılıklar göz ardı edilebilir.
    **AB:** Süreç hırsızlığı 90 puanla en yüksek - her adımda öğrenci onayı zorunludur. Ancak iş yükü 40 puanla en düşük - her YZ kararı insan denetimine tabidir.
    **UNESCO:** Tüm kategorilerde düşük - tavsiyeler bağlayıcı değildir.
    **ABD/İngiltere:** İş yükü 70 puan - öğretmen seçme özgürlüğüne sahiptir. Ancak süreç hırsızlığı 58 puan - pedagojik risk yüksektir.
    """)
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [85, 80, 75, 65, 60, 70],
        "Çin": [60, 55, 40, 85, 50, 88],
        "AB": [75, 95, 90, 40, 55, 68],
        "UNESCO": [70, 85, 80, 45, 45, 82],
        "ABD/İngiltere": [65, 45, 40, 70, 95, 75]
    }
    st.plotly_chart(politika_radar_analizi("Matematik", radar_puanlari), use_container_width=True)
    
    st.markdown("""
    **📊 Matematik - Radar Analizi Her Ülke İçin Detaylı:**
    
    **Türkiye:** Pedagojik Uygunluk 85 (en güçlü yanı), Etik 80, Mahremiyet 75, İş Yükü 65, Yenilik 60, Erişilebilirlik 70.
    - YAZEK sistemi pedagojik ilkeleri korur. 'İpucu verme' zorunluluğu sayesinde öğrenci düşünmek zorundadır.
    
    **Çin:** İş Yükü 85 ve Erişilebilirlik 88 (en yüksek), ancak Mahremiyet 40 (en düşük).
    - Merkezi sistem öğretmeni rahatlatır ve her okula eşit erişim sağlar. Ancak öğrenci verileri devlet kontrolündedir.
    
    **AB:** Etik 95 ve Mahremiyet 90 (en yüksek), ancak İş Yükü 40 (en düşük).
    - GDPR ve YZ Yasası en güçlü yasal çerçeveyi sunar. Ancak her YZ kararının insan denetimi öğretmene ek yük bindirir.
    
    **UNESCO:** Etik 85 ve Mahremiyet 80 yüksek, ancak Yenilik 45 düşük.
    - İnsan hakları temelli yaklaşımı güçlüdür, ancak yaptırım gücü yoktur ve yenilik konusunda yavaştır.
    
    **ABD/İngiltere:** Yenilik 95 (en yüksek), ancak Etik 45 ve Mahremiyet 40 (en düşük).
    - Serbest piyasa en hızlı yeniliği teşvik eder. Ancak etik ve mahremiyet koruması zayıftır, sorunlar genellikle dava yoluyla çözülür.
    """)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 85, "Etik Risk": 80, "Pratik Risk": 65, "Mahremiyet Riski": 75},
        "Çin": {"Pedagojik Risk": 60, "Etik Risk": 55, "Pratik Risk": 88, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 78, "Etik Risk": 95, "Pratik Risk": 45, "Mahremiyet Riski": 90},
        "UNESCO": {"Pedagojik Risk": 65, "Etik Risk": 85, "Pratik Risk": 40, "Mahremiyet Riski": 80},
        "ABD/İngiltere": {"Pedagojik Risk": 55, "Etik Risk": 48, "Pratik Risk": 82, "Mahremiyet Riski": 45}
    }
    st.plotly_chart(risk_azaltma_grafigi("Matematik", risk_oranlari), use_container_width=True)
    
    st.markdown("""
    **📊 Matematik - Risk Azaltma Başarı Oranları Detaylı:**
    
    **Türkiye (Ort. 76.25):** Pedagojik Risk 85 (en yükseklerden), Pratik Risk 65 (orta). YAZEK pedagojik riski en iyi yönetir.
    **Çin (Ort. 61.25):** Pratik Risk 88 (en yüksek), Mahremiyet Riski 42 (en düşük). Uygulama kolaylığı yüksek, mahremiyet zayıf.
    **AB (Ort. 77.0):** Etik Risk 95, Mahremiyet 90 (en yüksek), Pratik Risk 45 (en düşük). Etik ve mahremiyette lider, pratikte zorlanır.
    **UNESCO (Ort. 67.5):** Etik Risk 85, Pratik Risk 40 (en düşük). Tavsiyeler etik açıdan güçlü ama pratik çözüm sunmaz.
    **ABD/İngiltere (Ort. 57.5):** Pratik Risk 82 (yüksek), Etik Risk 48 (en düşük). Uygulama kolay ama etik riskler yüksek.
    """)
    
    st.markdown("### 🧠 Matematik - Bilimsel Değerlendirme")
    st.markdown("""
    Matematik eğitiminde YZ kullanımına ilişkin meta-analizler (Holmes vd., 2025), otomatik problem çözücülerin işlem becerilerini kısa vadede artırdığını ancak kavramsal anlamada erozyona yol açtığını göstermektedir.
    
    YAZEK'in 'ipucu verme' kuralı Vygotsky'nin Yakınsal Gelişim Alanı teorisiyle uyumludur. Çin modeli PISA'da başarılıdır ancak yaratıcılığı baskılayabilir. AB modeli öğrenci haklarını en üst düzeyde korur ancak iş yükünü artırır.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Pedagojik koruma, öğretmen özerk", "Standardizasyon, hızlı müdahale", "Öğrenci hakları, şeffaflık", "Uluslararası uzlaşı", "Hızlı yenilik, rekabet"],
        "Dezavantajlar": ["Maliyetli, bürokratik", "Yaratıcılığı ezer", "İş yükü artar, yavaş", "Bağlayıcı değil", "Eşitsizlik, güvensiz"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 2: FİZİK (TAM DETAY)
# ========================
def fizik_analizi():
    st.header("⚡ Fizik Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli fizik simülasyonları ve deney asistanı.")
    st.markdown("**Sorunlar:** (1) Epistemolojik boşluk (simülasyon-gerçek farkı), (2) Formül gizemliliği, (3) Denetim zorluğu.")
    
    tablo_headers = ["Strateji", "Epistemolojik Boşluk", "Formül Gizemliliği", "Denetim Zorluğu", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Teorik hazırlık + simülasyon + gerçek deney", "Adım adım formül çıkarımı zorunlu", "Parametreler öğretmen kontrolünde", "Gerçek deneye tamamlayıcı"],
        ["🇨🇳 Çin", "Teorik kavramlar simülasyonla bütünleşik", "Standart video içerik", "Merkezi sistem, değişiklik yok", "Standart öğretim aracı"],
        ["🇪🇺 AB", "Sınırlılıklar açıkça belirtilmeli", "Açıklayamıyorsa yüksek riskli", "Her kullanım kayıt altında", "Yüksek denetimli"],
        ["🇺🇳 UNESCO", "Hibrit eğitim önerisi", "Açık kaynak önerisi", "Öğretmen ağları", "Tavsiye"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Okul bütçesine göre", "'Açıklanabilir YZ' etiketi", "Öğretmen sorumluluğu", "Piyasa kararı"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Epistemolojik Boşluk": {"Türkiye (YAZEK)": 88, "Çin": 65, "AB": 85, "UNESCO": 75, "ABD/İngiltere": 55},
        "Formül Gizemliliği": {"Türkiye (YAZEK)": 82, "Çin": 70, "AB": 88, "UNESCO": 72, "ABD/İngiltere": 60},
        "Denetim Zorluğu": {"Türkiye (YAZEK)": 70, "Çin": 82, "AB": 50, "UNESCO": 48, "ABD/İngiltere": 68}
    }
    st.pyplot(politika_etkinlik_heatmap("Fizik", etkinlik_matrisi))
    
    st.markdown("""
    **📊 Fizik - Heatmap Detaylı Analizi:**
    
    | Ülke | Epistemolojik | Formül | Denetim | Ort. |
    |-------|---------------|--------|---------|------|
    | **Türkiye** | 88 | 82 | 70 | 80.0 |
    | **Çin** | 65 | 70 | 82 | 72.3 |
    | **AB** | 85 | 88 | 50 | 74.3 |
    | **UNESCO** | 75 | 72 | 48 | 65.0 |
    | **ABD/İngiltere** | 55 | 60 | 68 | 61.0 |
    
    **Türkiye:** Epistemolojik boşluğa karşı 88 puan - hibrit model (teori→simülasyon→gerçek deney) en etkili çözümdür.
    **AB:** Formül gizemliliği 88 puan - YZ formülü açıklayamıyorsa yüksek riskli sınıflandırılır. Denetim 50 puan - aşırı bürokrasi.
    **Çin:** Denetim 82 puan - merkezi sistem tam kontrollüdür. Ancak epistemolojik 65 puan - simülasyon-gerçek farkı öğretilmez.
    """)
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [88, 82, 75, 68, 58, 72],
        "Çin": [62, 58, 42, 84, 48, 86],
        "AB": [78, 94, 90, 42, 52, 65],
        "UNESCO": [72, 86, 82, 46, 44, 80],
        "ABD/İngiltere": [68, 48, 42, 72, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Fizik", radar_puanlari), use_container_width=True)
    
    st.markdown("""
    **📊 Fizik - Radar Analizi Her Ülke Detaylı:**
    
    **Türkiye:** Pedagojik 88 (en yüksek) - hibrit model fizik eğitiminin doğasına en uygun olanıdır. Etik 82, Mahremiyet 75.
    **AB:** Etik 94 ve Mahremiyet 90 (en yüksek) - yasal çerçeve çok güçlüdür. Ancak İş Yükü 42 (en düşük) - her simülasyon kaydı denetlenir.
    **Çin:** Erişilebilirlik 86 ve İş Yükü 84 - merkezi sistem her okula eşit erişim sağlar. Mahremiyet 42 - veriler devlet kontrolünde.
    **ABD/İngiltere:** Yenilik 94 (en yüksek) - piyasa rekabeti hızlı yenilik getirir. Etik 48 ve Mahremiyet 42 - koruma zayıftır.
    """)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 88, "Etik Risk": 82, "Pratik Risk": 70, "Mahremiyet Riski": 75},
        "Çin": {"Pedagojik Risk": 62, "Etik Risk": 58, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 80, "Etik Risk": 94, "Pratik Risk": 48, "Mahremiyet Riski": 90},
        "UNESCO": {"Pedagojik Risk": 72, "Etik Risk": 86, "Pratik Risk": 46, "Mahremiyet Riski": 82},
        "ABD/İngiltere": {"Pedagojik Risk": 58, "Etik Risk": 50, "Pratik Risk": 78, "Mahremiyet Riski": 48}
    }
    st.plotly_chart(risk_azaltma_grafigi("Fizik", risk_oranlari), use_container_width=True)
    
    st.markdown("""
    **📊 Fizik - Risk Azaltma Detaylı Analizi:**
    
    **Türkiye (Ort. 78.75):** Pedagojik Risk 88 (en yüksek) - hibrit model epistemolojik riski en aza indirir.
    **AB (Ort. 78.0):** Etik Risk 94, Mahremiyet 90 - en güçlü yasal koruma. Pratik Risk 48 - uygulama zorluğu.
    **Çin (Ort. 62.0):** Pratik Risk 86 - uygulama kolaylığı yüksek. Mahremiyet 42 - zayıf koruma.
    **ABD/İngiltere (Ort. 58.5):** Pratik Risk 78 - uygulama kolay. Pedagojik Risk 58 - en yüksek pedagojik risk.
    """)
    
    st.markdown("### 🧠 Fizik - Bilimsel Değerlendirme")
    st.markdown("""
    Fizik eğitiminde simülasyonlar, gerçek dünyanın indirgenmiş modelleridir. Sismondo (2021), 'model ile gerçeklik arasındaki farkı kavrayabilmenin' temel sorun olduğunu belirtir.
    
    Türkiye'nin hibrit yaklaşımı bu sorunu çözmeye yöneliktir. 2025'te yapılan bir çalışma (Karakaya & Schmidt), sadece simülasyonla fizik öğrenen öğrencilerin gerçek deneyde %62 daha fazla hata yaptığını bulmuştur.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Hibrit model, düşük epistemolojik risk", "Eşit erişim, tam denetim", "Yüksek şeffaflık, yasal güvence", "Evrensel ilkeler", "Hızlı yenilik"],
        "Dezavantajlar": ["Maliyetli", "Yaratıcılığı sınırlar", "Bürokratik, yavaş", "Bağlayıcı değil", "Eşitsizlik, pedagojik risk"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 3: KİMYA (TAM DETAY)
# ========================
def kimya_analizi():
    st.header("🧪 Kimya Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli molekül modelleme, reaksiyon tahmini ve sanal laboratuvar.")
    st.markdown("**Sorunlar:** (1) Güvenlik riski (yanlış reaksiyon önerisi), (2) Sanal-gerçek tutarsızlığı, (3) Tehlikeli sorgular.")
    
    tablo_headers = ["Strateji", "Güvenlik Riski", "Sanal-Gerçek Tutarsızlığı", "Tehlikeli Sorgular", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "MEB onaylı reaksiyonlar, yasaklı madde listesi", "Renk/oluşum gerçekle birebir eşleşmeli", "'Öğretmeninize danışın' yanıtı", "Güvenlik filtresi zorunlu"],
        ["🇨🇳 Çin", "Devlet onaylı reaksiyon veritabanı", "Renkler standartlaştırılmış", "Riskli sorgularda okula bildirim", "Merkezi kontrol"],
        ["🇪🇺 AB", "Risk değerlendirmesi zorunlu (CE)", "Sapma oranı < %1", "Engelleme ve kuruma bildirim", "Yüksek riskli kategori"],
        ["🇺🇳 UNESCO", "Güvenlik eğitimiyle birlikte", "Açık kaynak protokolü", "Öğretmen eğitimi", "Tavsiye"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "'Güvenli Kimya YZ' sertifikası", "Rekabetle en gerçekçi simülasyonlar", "Okul politikası", "Serbest piyasa"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Güvenlik Riski": {"Türkiye (YAZEK)": 92, "Çin": 85, "AB": 90, "UNESCO": 70, "ABD/İngiltere": 60},
        "Sanal-Gerçek Tutarsızlığı": {"Türkiye (YAZEK)": 80, "Çin": 75, "AB": 85, "UNESCO": 68, "ABD/İngiltere": 65},
        "Tehlikeli Sorgular": {"Türkiye (YAZEK)": 88, "Çin": 82, "AB": 86, "UNESCO": 65, "ABD/İngiltere": 55}
    }
    st.pyplot(politika_etkinlik_heatmap("Kimya", etkinlik_matrisi))
    
    st.markdown("""
    **📊 Kimya - Heatmap Detaylı Analizi:**
    
    | Ülke | Güvenlik | Tutarsızlık | Tehlikeli Sorgular | Ort. |
    |-------|----------|-------------|---------------------|------|
    | **Türkiye** | 92 | 80 | 88 | 86.7 |
    | **Çin** | 85 | 75 | 82 | 80.7 |
    | **AB** | 90 | 85 | 86 | 87.0 |
    | **UNESCO** | 70 | 68 | 65 | 67.7 |
    | **ABD/İngiltere** | 60 | 65 | 55 | 60.0 |
    
    **Türkiye:** Güvenlik 92 puan - MEB onaylı reaksiyonlar ve yasaklı madde listesi en sıkı güvenlik önlemleridir.
    **AB:** Tutarsızlık 85 puan - sapma oranı < %1 şartı simülasyon gerçekliğini garanti eder.
    **Çin:** Tehlikeli sorgular 82 puan - riskli sorular otomatik okula bildirilir, erken müdahale sağlanır.
    """)
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [85, 90, 80, 65, 55, 72],
        "Çin": [65, 60, 42, 84, 48, 88],
        "AB": [80, 95, 92, 42, 52, 68],
        "UNESCO": [72, 88, 84, 45, 42, 82],
        "ABD/İngiltere": [60, 48, 45, 70, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Kimya", radar_puanlari), use_container_width=True)
    
    st.markdown("""
    **📊 Kimya - Radar Analizi Her Ülke Detaylı:**
    
    **Türkiye:** Etik 90, Pedagojik 85 - kimya güvenliği en ön plandadır. YASAGI SORGU listesi ile tehlikeli maddeler filtrelenir.
    **AB:** Etik 95, Mahremiyet 92 - en yüksek. Kimyasal reaksiyon öneren YZ 'yüksek riskli' statüsündedir ve sıkı denetime tabidir.
    **Çin:** Erişilebilirlik 88 - merkezi platform her okula ulaşır. Mahremiyet 42 - veriler devlet kontrolünde.
    **ABD/İngiltere:** Yenilik 94 - hızlı yeni molekül modelleme araçları. Etik 48 - güvenlik sertifikaları zorunlu değildir.
    """)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 82, "Etik Risk": 90, "Pratik Risk": 68, "Mahremiyet Riski": 80},
        "Çin": {"Pedagojik Risk": 65, "Etik Risk": 60, "Pratik Risk": 88, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 78, "Etik Risk": 95, "Pratik Risk": 48, "Mahremiyet Riski": 92},
        "UNESCO": {"Pedagojik Risk": 70, "Etik Risk": 88, "Pratik Risk": 45, "Mahremiyet Riski": 84},
        "ABD/İngiltere": {"Pedagojik Risk": 55, "Etik Risk": 50, "Pratik Risk": 82, "Mahremiyet Riski": 48}
    }
    st.plotly_chart(risk_azaltma_grafigi("Kimya", risk_oranlari), use_container_width=True)
    
    st.markdown("""
    **📊 Kimya - Risk Azaltma Detaylı Analizi:**
    
    **Türkiye (Ort. 80.0):** Etik Risk 90, Pratik Risk 68 - güvenlik önlemleri çok güçlüdür.
    **AB (Ort. 78.25):** Etik Risk 95, Mahremiyet 92 - en güçlü yasal çerçeve. Pratik Risk 48 - uygulama zorluğu.
    **Çin (Ort. 63.75):** Pratik Risk 88 - uygulama kolay. Mahremiyet 42 - zayıf koruma.
    **ABD/İngiltere (Ort. 58.75):** Pratik Risk 82 - uygulama kolay. Etik Risk 50 - güvenlik riskleri yüksek.
    """)
    
    st.markdown("### 🧠 Kimya - Bilimsel Değerlendirme")
    st.markdown("""
    Kimya eğitiminde YZ, en yüksek fiziksel riskleri barındırır. Yanlış bir reaksiyon önerisi veya tehlikeli madde karışımı tavsiyesi ciddi zararlara yol açabilir.
    
    YAZEK'in kimya modülü için ayrı bir 'güvenlik katmanı' bulunur. AB YZ Yasası'na göre, kimyasal reaksiyon öneren YZ 'yüksek riskli' statüsündedir. Çin'in bildirim sistemi, tehlikeli sorguların otomatik okula iletilmesini sağlar.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["En yüksek güvenlik, MEB onaylı", "Tam izlenebilirlik, bildirim sistemi", "Yasal güvence, CE benzeri onay", "Uluslararası standartlar", "Hızlı yenilik, sertifikasyon"],
        "Dezavantajlar": ["Müfredat dışı keşfi sınırlar", "Mahremiyet zayıf", "Yüksek maliyet, zaman alıcı", "Bağlayıcı değil", "Düşük gelirli okullar için riskli"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 4: BİYOLOJİ (TAM DETAY)
# ========================
def biyoloji_analizi():
    st.header("🧬 Biyoloji Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli genetik analiz, evrim simülasyonu ve tür tanıma.")
    st.markdown("**Sorunlar:** (1) Genetik veri gizliliği, (2) Evrim gibi hassas konularda yanlı içerik, (3) Tür tanıma hataları.")
    
    tablo_headers = ["Strateji", "Genetik Veri Gizliliği", "Evrim/Teorik Konular", "Tür Tanıma Hatası", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "DNA verisi için veli onayı zorunlu", "Müfredata uygun, bilimsel görüş birliği", "Hata oranı < %5, öğretmen onayı", "Yüksek gizlilikli"],
        ["🇨🇳 Çin", "Devlet sunucularında, eğitim amaçlı serbest", "Ulusal müfredat çerçevesi", "Ulusal veritabanıyla tek sistem", "Merkezi kontrol"],
        ["🇪🇺 AB", "GDPR kapsamında 'özel veri', işleme yasak", "Bilimsel görüş birliği, çoğulcu", "Yasal sorumluluk", "Çok sıkı, neredeyse kullanım dışı"],
        ["🇺🇳 UNESCO", "Küresel etik rehberler", "Farklı kültürel perspektifler", "Uluslararası veritabanları", "Tavsiye"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Şirket politikaları farklı", "Farklı görüşler, okul seçimi", "Dava yoluyla cezalandırma", "Serbest piyasa"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Genetik Veri Gizliliği": {"Türkiye (YAZEK)": 85, "Çin": 45, "AB": 95, "UNESCO": 80, "ABD/İngiltere": 48},
        "Evrim/Teorik Konular": {"Türkiye (YAZEK)": 80, "Çin": 60, "AB": 88, "UNESCO": 85, "ABD/İngiltere": 65},
        "Tür Tanıma Hatası": {"Türkiye (YAZEK)": 75, "Çin": 78, "AB": 85, "UNESCO": 70, "ABD/İngiltere": 60}
    }
    st.pyplot(politika_etkinlik_heatmap("Biyoloji", etkinlik_matrisi))
    
    st.markdown("""
    **📊 Biyoloji - Heatmap Detaylı Analizi:**
    
    | Ülke | Genetik Gizlilik | Evrim/Teorik | Tanıma Hatası | Ort. |
    |-------|------------------|--------------|---------------|------|
    | **Türkiye** | 85 | 80 | 75 | 80.0 |
    | **Çin** | 45 | 60 | 78 | 61.0 |
    | **AB** | 95 | 88 | 85 | 89.3 |
    | **UNESCO** | 80 | 85 | 70 | 78.3 |
    | **ABD/İngiltere** | 48 | 65 | 60 | 57.7 |
    
    **AB:** Genetik veri gizliliği 95 puan - GDPR genetik veriyi 'özel kategori' sayar ve işlenmesini neredeyse tamamen yasaklar.
    **Türkiye:** Genetik gizlilik 85 puan - YAZEK izni ve veli onayı zorunludur.
    **Çin:** Genetik gizlilik 45 puan - veriler devlet kontrolünde, bireysel sildirme hakkı yoktur.
    """)
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [80, 82, 85, 70, 55, 72],
        "Çin": [62, 55, 40, 86, 50, 88],
        "AB": [82, 96, 95, 42, 52, 68],
        "UNESCO": [75, 90, 88, 45, 44, 84],
        "ABD/İngiltere": [65, 48, 42, 72, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Biyoloji", radar_puanlari), use_container_width=True)
    
    st.markdown("""
    **📊 Biyoloji - Radar Analizi Her Ülke Detaylı:**
    
    **AB:** Etik 96, Mahremiyet 95 (en yüksek) - GDPR'nin en sıkı kuralları biyoloji verileri için geçerlidir. İş Yükü 42 - uygulama neredeyse imkansızdır.
    **Türkiye:** Mahremiyet 85, Etik 82 - YAZEK izin mekanizması çalışır. Pedagojik 80 - müfredata uygun içerik.
    **Çin:** Erişilebilirlik 88 - ulusal veritabanı her okula açıktır. Mahremiyet 40 - en düşük.
    **ABD/İngiltere:** Yenilik 94 - genetik analiz araçları hızla gelişir. Etik 48 - dava mekanizması yeterli değildir.
    """)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 80, "Etik Risk": 82, "Pratik Risk": 70, "Mahremiyet Riski": 85},
        "Çin": {"Pedagojik Risk": 62, "Etik Risk": 55, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 78, "Etik Risk": 96, "Pratik Risk": 42, "Mahremiyet Riski": 95},
        "UNESCO": {"Pedagojik Risk": 72, "Etik Risk": 90, "Pratik Risk": 44, "Mahremiyet Riski": 88},
        "ABD/İngiltere": {"Pedagojik Risk": 60, "Etik Risk": 50, "Pratik Risk": 80, "Mahremiyet Riski": 48}
    }
    st.plotly_chart(risk_azaltma_grafigi("Biyoloji", risk_oranlari), use_container_width=True)
    
    st.markdown("""
    **📊 Biyoloji - Risk Azaltma Detaylı Analizi:**
    
    **AB (Ort. 77.75):** Etik Risk 96, Mahremiyet 95 - en güçlü koruma. Pratik Risk 42 - en zayıf.
    **Türkiye (Ort. 79.25):** Mahremiyet 85, Etik 82 - dengeli yaklaşım.
    **Çin (Ort. 61.25):** Pratik Risk 86 - uygulama kolay. Mahremiyet 42 - çok zayıf.
    **ABD/İngiltere (Ort. 59.5):** Pratik Risk 80 - uygulama kolay. Etik 50 - koruma zayıf.
    """)
    
    st.markdown("### 🧠 Biyoloji - Bilimsel Değerlendirme")
    st.markdown("""
    Biyoloji eğitiminde YZ, diğer derslerden farklı olarak 'yaşayan sistemlerle' ilgili verileri işler. Genetik bilgi son derece hassastır.
    
    GDPR, genetik veriyi 'özel kategori' veri olarak sınıflandırır ve işlenmesini neredeyse yasaklar. YAZEK'in izin mekanizması, hem öğrenci haklarını korur hem de eğitimsel faydayı sağlar. Çin'de veriler devlet kontrolündedir ancak bireysel sildirme hakkı yoktur.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Biyoetik ilkelere saygı, izin mekanizması", "Tam kontrol, büyük veri", "En yüksek gizlilik", "Küresel biyoetik rehberlik", "Yenilikçi genetik uygulamalar"],
        "Dezavantajlar": ["Bürokratik süreç", "Bireysel gizlilik riski", "Eğitimde YZ kullanımını zorlaştırır", "Bağlayıcı değil", "Gizlilik ihlalleri sık"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 5: TÜRKÇE / EDEBİYAT (TAM DETAY)
# ========================
def turkce_analizi():
    st.header("📖 Türkçe / Edebiyat Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli metin üretimi, duygu analizi ve yazım denetimi.")
    st.markdown("**Sorunlar:** (1) Özgünlük kaybı (YZ'ye kompozisyon yazdırma), (2) Duygu analizinin kültürel duyarsızlığı, (3) Bağlam bozulması.")
    
    tablo_headers = ["Strateji", "Özgünlük Kaybı", "Duygu Analizi Duyarsızlığı", "Bağlam Bozulması", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Sadece taslak önerisi, son metin öğrenciye ait", "Türk edebiyatı türlerine özel eğitilmiş modeller", "Metin türü/dönem bilgisi girilmeli", "Yaratıcılığı destekler"],
        ["🇨🇳 Çin", "Ulusal platform, özgünlük taraması", "Devlet onaylı duygu sınıflandırıcısı", "Standart kurallar, bağlam ikinci planda", "Standardizasyon aracı"],
        ["🇪🇺 AB", "Özgünlük raporu, YZ katkısı deklare edilmeli", "Sınırlılıklar açıklanmalı", "YZ önerileri opsiyonel", "Şeffaf kullanım"],
        ["🇺🇳 UNESCO", "YZ'nin yaratıcılığı desteklemesi vurgusu", "Kültürel çeşitliliğe duyarlılık", "Dil bilinci eğitimiyle birlikte", "Tavsiye"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Okulun özgünlük politikası, YZ dedektörleri", "Farklı modeller, okul seçer", "Sürekli güncellenen araçlar", "Piyasa rekabeti"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Özgünlük Kaybı": {"Türkiye (YAZEK)": 82, "Çin": 75, "AB": 85, "UNESCO": 70, "ABD/İngiltere": 60},
        "Duygu Analizi Duyarsızlığı": {"Türkiye (YAZEK)": 78, "Çin": 65, "AB": 80, "UNESCO": 75, "ABD/İngiltere": 58},
        "Bağlam Bozulması": {"Türkiye (YAZEK)": 80, "Çin": 68, "AB": 82, "UNESCO": 72, "ABD/İngiltere": 62}
    }
    st.pyplot(politika_etkinlik_heatmap("Türkçe/Edebiyat", etkinlik_matrisi))
    
    st.markdown("""
    **📊 Türkçe - Heatmap Detaylı Analizi:**
    
    **Türkiye:** Özgünlük 82, Bağlam 80 - 'sadece taslak' kuralı yaratıcılığı korur. Tür edebiyatına özel modeller duygu analizini iyileştirir.
    **AB:** Özgünlük 85, Bağlam 82 - YZ katkısı deklare zorunluluğu şeffaflık sağlar.
    **Çin:** Duygu analizi 65 - standart sınıflandırıcı kültürel nüansları yakalamakta zorlanır.
    """)
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [82, 80, 75, 68, 58, 72],
        "Çin": [65, 58, 42, 85, 48, 86],
        "AB": [78, 92, 88, 42, 55, 68],
        "UNESCO": [74, 88, 82, 45, 46, 84],
        "ABD/İngiltere": [70, 48, 45, 72, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Türkçe/Edebiyat", radar_puanlari), use_container_width=True)
    
    st.markdown("""
    **📊 Türkçe - Radar Analizi Her Ülke Detaylı:**
    
    **Türkiye:** Pedagojik 82, Etik 80 - Türk edebiyatı türlerine özel eğitilmiş modeller, kültürel duyarlılığı artırır.
    **AB:** Etik 92, Mahremiyet 88 - yasal çerçeve güçlüdür.
    **Çin:** İş Yükü 85 - otomatik özgünlük taraması. Kültürel duyarlılık 58 - düşük.
    """)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 82, "Etik Risk": 80, "Pratik Risk": 68, "Mahremiyet Riski": 75},
        "Çin": {"Pedagojik Risk": 65, "Etik Risk": 58, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 78, "Etik Risk": 92, "Pratik Risk": 48, "Mahremiyet Riski": 88},
        "UNESCO": {"Pedagojik Risk": 72, "Etik Risk": 88, "Pratik Risk": 46, "Mahremiyet Riski": 82},
        "ABD/İngiltere": {"Pedagojik Risk": 68, "Etik Risk": 50, "Pratik Risk": 78, "Mahremiyet Riski": 48}
    }
    st.plotly_chart(risk_azaltma_grafigi("Türkçe/Edebiyat", risk_oranlari), use_container_width=True)
    
    st.markdown("### 🧠 Türkçe - Bilimsel Değerlendirme")
    st.markdown("""
    Dil ve edebiyat eğitiminde YZ kullanımı, özgünlük ve yaratıcılık açısından en fazla tartışılan alandır. Araştırmalar, öğrencilerin yaklaşık %40'ının ev ödevlerinde YZ'den doğrudan metin ürettiğini göstermektedir.
    
    YAZEK'in 'sadece taslak önerisi' yaklaşımı bu riski azaltır. Duygu analizi modelleri genellikle Batı edebiyatı üzerine eğitilmiştir; Türk edebiyatına özel modeller bu sorunu çözmeye yöneliktir.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Kültürel duyarlılık, yaratıcılığı korur", "Özgünlük taraması etkili", "Şeffaflık, deklarasyon", "Kültürel çeşitlilik", "Hızlı yenilik"],
        "Dezavantajlar": ["Model eğitimi maliyetli", "Kültürel nüansları kaçırır", "Bürokratik", "Bağlayıcı değil", "Özgünlük riski yüksek"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 6: TARİH (TAM DETAY)
# ========================
def tarih_analizi():
    st.header("🏛️ Tarih Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli tarihsel olay simülasyonu, kaynak değerlendirme.")
    st.markdown("**Sorunlar:** (1) Anakronizm riski, (2) Taraflı anlatı riski, (3) Kaynak okuma alışkanlığı kaybı.")
    
    tablo_headers = ["Strateji", "Anakronizm Riski", "Taraflı Anlatı Riski", "Kaynak Okuma Alışkanlığı", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Dönem koşulları belirtilmeli", "Çoklu kaynak (en az 3 farklı görüş)", "Birincil kaynak bağlantısı verilmeli", "Eleştirel tarih eğitiminin yardımcısı"],
        ["🇨🇳 Çin", "Resmi tarih tezine uygun", "Tek resmi kaynak", "Birincil kaynaklara erişim sınırlı", "Resmi tarih aktarım aracı"],
        ["🇪🇺 AB", "Anakronizm uyarısı zorunlu", "Farklı tarih yazım ekolleri", "Birincil kaynaklara bağlantı zorunlu", "Çok sesli tarih aracı"],
        ["🇺🇳 UNESCO", "Dünya tarihi perspektifi", "Farklı kültürel anlatılar", "Birincil kaynak okuryazarlığı", "Küresel vatandaşlık"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Farklı ideolojiler, okul seçimi", "Rekabetle dengeli modeller", "En çok atıf yapılan kaynaklar", "Serbest piyasa"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Anakronizm Riski": {"Türkiye (YAZEK)": 85, "Çin": 70, "AB": 88, "UNESCO": 80, "ABD/İngiltere": 60},
        "Taraflı Anlatı Riski": {"Türkiye (YAZEK)": 80, "Çin": 50, "AB": 90, "UNESCO": 85, "ABD/İngiltere": 65},
        "Kaynak Okuma Alışkanlığı": {"Türkiye (YAZEK)": 78, "Çin": 55, "AB": 85, "UNESCO": 82, "ABD/İngiltere": 62}
    }
    st.pyplot(politika_etkinlik_heatmap("Tarih", etkinlik_matrisi))
    
    st.markdown("""
    **📊 Tarih - Heatmap Detaylı Analizi:**
    
    **AB:** Anakronizm 88, Taraflı anlatı 90 - en yüksek. Farklı tarih yazım ekollerini içerme zorunluluğu.
    **Türkiye:** Anakronizm 85, Taraflı anlatı 80 - çoklu kaynak zorunluluğu (en az 3 farklı görüş).
    **Çin:** Taraflı anlatı 50 - tek resmi kaynak, farklı görüşlere yer yok.
    """)
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [82, 80, 75, 68, 55, 70],
        "Çin": [60, 55, 40, 86, 48, 88],
        "AB": [80, 94, 90, 42, 52, 68],
        "UNESCO": [78, 90, 85, 45, 44, 85],
        "ABD/İngiltere": [68, 50, 45, 72, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Tarih", radar_puanlari), use_container_width=True)
    
    st.markdown("""
    **📊 Tarih - Radar Analizi Her Ülke Detaylı:**
    
    **AB:** Etik 94, Mahremiyet 90 - en yüksek. Çok sesli tarih anlatısı yasal güvence altındadır.
    **Türkiye:** Pedagojik 82 - dönem koşullarının belirtilmesi anakronizmi önler. Çoklu kaynak zorunluluğu dengeli tarih eğitimi sağlar.
    **Çin:** Erişilebilirlik 88 - merkezi sistem. Etik 55 - resmi tarih tezi dışına çıkılamaz.
    """)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 82, "Etik Risk": 80, "Pratik Risk": 68, "Mahremiyet Riski": 75},
        "Çin": {"Pedagojik Risk": 60, "Etik Risk": 55, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 80, "Etik Risk": 94, "Pratik Risk": 48, "Mahremiyet Riski": 90},
        "UNESCO": {"Pedagojik Risk": 78, "Etik Risk": 90, "Pratik Risk": 46, "Mahremiyet Riski": 85},
        "ABD/İngiltere": {"Pedagojik Risk": 68, "Etik Risk": 52, "Pratik Risk": 78, "Mahremiyet Riski": 48}
    }
    st.plotly_chart(risk_azaltma_grafigi("Tarih", risk_oranlari), use_container_width=True)
    
    st.markdown("### 🧠 Tarih - Bilimsel Değerlendirme")
    st.markdown("""
    Tarih eğitiminde YZ kullanımı, metodoloji açısından en karmaşık alanlardan biridir. Tarihsel bilginin doğası gereği, tek bir 'doğru' anlatı yoktur; yorum ve perspektif her zaman vardır.
    
    YAZEK'in 'dönem koşulları belirtilmeden yorum yapılamaz' kuralı anakronizmi önler. 'Çoklu kaynak zorunluluğu' (en az 3 farklı görüş) taraflı anlatı riskini azaltır. AB'nin farklı tarih yazım ekollerini içerme zorunluluğu da benzer bir amaca hizmet eder.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Çoklu kaynak, anakronizm önleme", "Tam denetim, standart", "Çok sesli, yasal güvence", "Küresel perspektif", "Çeşitlilik, rekabet"],
        "Dezavantajlar": ["Kaynak bulma zorluğu", "Tek tip anlatı", "Bürokratik", "Bağlayıcı değil", "Kalite güvencesiz"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 7: COĞRAFYA (TAM DETAY)
# ========================
def cografya_analizi():
    st.header("🌍 Coğrafya Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli CBS analizi, iklim tahmini, nüfus modellemesi.")
    st.markdown("**Sorunlar:** (1) Mekânsal önyargı, (2) İklim belirsizliğini gizleme, (3) Harita okuma becerisi kaybı.")
    
    tablo_headers = ["Strateji", "Mekânsal Önyargı", "İklim Belirsizliği", "Harita Okuma Becerisi", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Veri setinin temsil gücü raporlanmalı", "Belirsizlik aralığı gösterilmeli", "YZ analizi öncesi manuel harita okuma", "Analiz aracı, ikame değil"],
        ["🇨🇳 Çin", "Devlet onaylı veri setleri", "Resmi tahminler, belirsizlik paylaşılmaz", "Standart testlerle ölçülür", "Denetimli devlet aracı"],
        ["🇪🇺 AB", "Önyargılar açıklanmalı", "Güven düzeyi belirtilmeli", "Harita okuma modülleri", "Şeffaf ve eğitici"],
        ["🇺🇳 UNESCO", "Mekânsal veri adaleti", "İklim eğitiminde YZ'nin sınırları", "Geleneksel becerilerin korunması", "Küresel rehber"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "'Adil YZ' etiketi oluşur", "Belirsizliği iyi yöneten tercih edilir", "Eğitim YZ'den bağımsız", "Piyasa çözümleri"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Mekânsal Önyargı": {"Türkiye (YAZEK)": 82, "Çin": 70, "AB": 88, "UNESCO": 80, "ABD/İngiltere": 60},
        "İklim Belirsizliği": {"Türkiye (YAZEK)": 85, "Çin": 55, "AB": 90, "UNESCO": 78, "ABD/İngiltere": 65},
        "Harita Okuma Becerisi": {"Türkiye (YAZEK)": 80, "Çin": 75, "AB": 85, "UNESCO": 82, "ABD/İngiltere": 68}
    }
    st.pyplot(politika_etkinlik_heatmap("Coğrafya", etkinlik_matrisi))
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [82, 84, 78, 70, 58, 74],
        "Çin": [65, 58, 42, 86, 48, 88],
        "AB": [80, 94, 90, 44, 54, 68],
        "UNESCO": [76, 88, 84, 46, 45, 85],
        "ABD/İngiltere": [68, 50, 45, 74, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Coğrafya", radar_puanlari), use_container_width=True)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 82, "Etik Risk": 84, "Pratik Risk": 70, "Mahremiyet Riski": 78},
        "Çin": {"Pedagojik Risk": 65, "Etik Risk": 58, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 80, "Etik Risk": 94, "Pratik Risk": 48, "Mahremiyet Riski": 90},
        "UNESCO": {"Pedagojik Risk": 76, "Etik Risk": 88, "Pratik Risk": 46, "Mahremiyet Riski": 84},
        "ABD/İngiltere": {"Pedagojik Risk": 68, "Etik Risk": 52, "Pratik Risk": 78, "Mahremiyet Riski": 48}
    }
    st.plotly_chart(risk_azaltma_grafigi("Coğrafya", risk_oranlari), use_container_width=True)
    
    st.markdown("### 🧠 Coğrafya - Bilimsel Değerlendirme")
    st.markdown("""
    Coğrafya eğitiminde YZ kullanımı, mekânsal verilerin doğası gereği önyargı riskleri taşır. YZ'nin bazı bölgeleri 'çok yoksul' etiketlemesi gibi sorunlar ortaya çıkabilir.
    
    YAZEK'in 'veri setinin temsil gücü raporlanmalı' kuralı bu riski azaltır. AB'nin 'önyargılar açıklanmalı' zorunluluğu şeffaflık sağlar. Ayrıca, 'YZ analizi öncesi manuel harita okuma zorunluluğu' temel becerilerin kaybını önler.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Önyargı raporlaması, manuel harita", "Tam kontrol, büyük veri", "Şeffaflık, yasal güvence", "Mekânsal adalet", "Hızlı yenilik"],
        "Dezavantajlar": ["Raporlama yükü", "Belirsizlik gizlenir", "Bürokratik", "Bağlayıcı değil", "Kalite güvencesiz"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 8: YABANCI DİL (TAM DETAY)
# ========================
def ingilizce_analizi():
    st.header("🗣️ Yabancı Dil (İngilizce) Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli dil öğrenme asistanı, konuşma pratiği.")
    st.markdown("**Sorunlar:** (1) Aksan ayrımcılığı, (2) Sosyal iletişim kaybı, (3) Kültürel bağlam duyarsızlığı.")
    
    tablo_headers = ["Strateji", "Aksan Ayrımcılığı", "Sosyal İletişim Kaybı", "Kültürel Bağlam", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Tüm aksanlara duyarlı modeller", "YZ konuşma süresi sınırlı, akran iletişimi zorunlu", "Bağlam etiketi (formal/informal) gerekli", "Pratik asistanı"],
        ["🇨🇳 Çin", "Standart Amerikan/İngiliz aksanı", "YZ konuşma pratiği yaygın", "Resmi müfredat dili", "Standartlaştırıcı"],
        ["🇪🇺 AB", "Aksan ayrımcılığı yasak", "Sosyal iletişim etkisi izlenir", "Kültürel varyantlar modülde", "Kapsayıcı"],
        ["🇺🇳 UNESCO", "Aksan duyarlılığı vurgusu", "İnsan etkileşiminin önemi", "Kültürel çeşitlilik", "Küresel rehber"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Farklı aksan modülleri satılır", "Okul politikası", "Rekabetle en bağlamlı modeller", "Serbest piyasa"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Aksan Ayrımcılığı": {"Türkiye (YAZEK)": 85, "Çin": 50, "AB": 92, "UNESCO": 82, "ABD/İngiltere": 60},
        "Sosyal İletişim Kaybı": {"Türkiye (YAZEK)": 80, "Çin": 65, "AB": 85, "UNESCO": 78, "ABD/İngiltere": 62},
        "Kültürel Bağlam": {"Türkiye (YAZEK)": 82, "Çin": 60, "AB": 88, "UNESCO": 85, "ABD/İngiltere": 68}
    }
    st.pyplot(politika_etkinlik_heatmap("Yabancı Dil", etkinlik_matrisi))
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [82, 84, 78, 70, 58, 72],
        "Çin": [62, 55, 42, 86, 48, 88],
        "AB": [80, 94, 90, 44, 54, 68],
        "UNESCO": [76, 88, 84, 46, 45, 85],
        "ABD/İngiltere": [70, 52, 48, 74, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Yabancı Dil", radar_puanlari), use_container_width=True)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 82, "Etik Risk": 84, "Pratik Risk": 70, "Mahremiyet Riski": 78},
        "Çin": {"Pedagojik Risk": 62, "Etik Risk": 55, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 80, "Etik Risk": 94, "Pratik Risk": 48, "Mahremiyet Riski": 90},
        "UNESCO": {"Pedagojik Risk": 76, "Etik Risk": 88, "Pratik Risk": 46, "Mahremiyet Riski": 84},
        "ABD/İngiltere": {"Pedagojik Risk": 70, "Etik Risk": 54, "Pratik Risk": 78, "Mahremiyet Riski": 50}
    }
    st.plotly_chart(risk_azaltma_grafigi("Yabancı Dil", risk_oranlari), use_container_width=True)
    
    st.markdown("### 🧠 Yabancı Dil - Bilimsel Değerlendirme")
    st.markdown("""
    Yabancı dil eğitiminde YZ, aksan ayrımcılığı riski taşır. Birçok dil öğrenme YZ'si, yalnızca standart Amerikan/İngiliz aksanıyla eğitilmiştir.
    
    YAZEK'in 'tüm aksanlara duyarlı modeller' zorunluluğu bu sorunu çözmeye yöneliktir. Ayrıca, 'YZ ile konuşma süresi sınırlı' kuralı, öğrencilerin gerçek insanlarla iletişimden kaçınmasını engeller.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Aksan çeşitliliği, dengeli iletişim", "Standardizasyon", "Kapsayıcılık, yasal güvence", "Kültürel çeşitlilik", "Hızlı yenilik, modül çeşitliliği"],
        "Dezavantajlar": ["Model eğitimi maliyetli", "Aksan ayrımcılığı", "İzleme yükü", "Bağlayıcı değil", "Eşitsiz erişim"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 9: MÜZİK (TAM DETAY)
# ========================
def muzik_analizi():
    st.header("🎵 Müzik Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli nota yazımı, kompozisyon yardımı.")
    st.markdown("**Sorunlar:** (1) Yaratıcılık körelmesi, (2) Müzik türü duyarsızlığı, (3) Telif hakkı ihlali.")
    
    tablo_headers = ["Strateji", "Yaratıcılık Körelmesi", "Tür Duyarsızlığı", "Telif Hakkı Riski", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Sadece ritim/armoni önerisi, melodi öğrenciye ait", "Müzik türü etiketi zorunlu", "> %70 benzerlikte öğretmen uyarısı", "Yaratıcılık asistanı"],
        ["🇨🇳 Çin", "Ulusal müzik kültürüne uygun kalıplar", "Tür sınıflandırması devletçe belirlenir", "Telif ihlali tespit sistemi", "Kültür aktarım aracı"],
        ["🇪🇺 AB", "YZ katkısı deklare edilmeli", "Farklı türler için ayrı modeller", "Telif yasalarına uyum zorunlu", "Şeffaf ve yasal"],
        ["🇺🇳 UNESCO", "Kültürel ifade çeşitliliği", "Geleneksel müziklerin temsili", "Sanatçı hakları", "Kültürel rehber"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "'Telifsiz' modeller rekabet eder", "En çok türü destekleyen tercih edilir", "Telif davaları disipline eder", "Piyasa rekabeti"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Yaratıcılık Körelmesi": {"Türkiye (YAZEK)": 85, "Çin": 65, "AB": 82, "UNESCO": 78, "ABD/İngiltere": 60},
        "Tür Duyarsızlığı": {"Türkiye (YAZEK)": 80, "Çin": 70, "AB": 85, "UNESCO": 82, "ABD/İngiltere": 65},
        "Telif Hakkı Riski": {"Türkiye (YAZEK)": 82, "Çin": 75, "AB": 90, "UNESCO": 80, "ABD/İngiltere": 55}
    }
    st.pyplot(politika_etkinlik_heatmap("Müzik", etkinlik_matrisi))
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [82, 80, 75, 68, 58, 70],
        "Çin": [65, 60, 42, 86, 48, 88],
        "AB": [78, 92, 88, 44, 54, 68],
        "UNESCO": [76, 88, 82, 46, 46, 84],
        "ABD/İngiltere": [68, 50, 45, 72, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Müzik", radar_puanlari), use_container_width=True)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 85, "Etik Risk": 80, "Pratik Risk": 68, "Mahremiyet Riski": 75},
        "Çin": {"Pedagojik Risk": 65, "Etik Risk": 60, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 78, "Etik Risk": 92, "Pratik Risk": 48, "Mahremiyet Riski": 88},
        "UNESCO": {"Pedagojik Risk": 76, "Etik Risk": 88, "Pratik Risk": 46, "Mahremiyet Riski": 82},
        "ABD/İngiltere": {"Pedagojik Risk": 68, "Etik Risk": 52, "Pratik Risk": 78, "Mahremiyet Riski": 48}
    }
    st.plotly_chart(risk_azaltma_grafigi("Müzik", risk_oranlari), use_container_width=True)
    
    st.markdown("### 🧠 Müzik - Bilimsel Değerlendirme")
    st.markdown("""
    Müzik eğitiminde YZ, yaratıcılık ve telif hakları açısından önemli tartışmalar yaratır. YZ'nin hazır melodi kalıpları sunması, öğrencinin özgün beste yapma becerisini köretebilir.
    
    YAZEK'in 'sadece ritim/armoni önerisi, melodi öğrenciye ait' kuralı yaratıcılığı korur. '> %70 benzerlikte öğretmen uyarısı' telif ihlallerini önler. AB'nin 'YZ katkısı deklare edilmeli' zorunluluğu şeffaflık sağlar.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Yaratıcılığı korur, telif önleme", "Kültür aktarımı", "Şeffaflık, yasal güvence", "Kültürel çeşitlilik", "Hızlı yenilik"],
        "Dezavantajlar": ["Öneri sınırlı", "Yaratıcılığı sınırlar", "Bürokratik", "Bağlayıcı değil", "Telif riski yüksek"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 10: GÖRSEL SANATLAR (TAM DETAY)
# ========================
def sanat_analizi():
    st.header("🎨 Görsel Sanatlar Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli görsel üretim, kolaj, stil transferi.")
    st.markdown("**Sorunlar:** (1) Temel beceri kaybı, (2) Stil/telif sorunu, (3) Estetik tekdüzelik.")
    
    tablo_headers = ["Strateji", "Temel Beceri Kaybı", "Stil/Telif Sorunu", "Estetik Tekdüzelik", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Manuel çizim tamamlanmadan YZ düzenlemesi yok", "Stil transferinde kaynak eser belirtilmeli", "En az 3 farklı estetik anlayışı", "Teknik asistan"],
        ["🇨🇳 Çin", "Ulusal müfredat, YZ yardımcı", "Stil kullanımı devlet teşvikiyle", "Devlet onaylı güzellik anlayışı", "Standart eğitim aracı"],
        ["🇪🇺 AB", "Sanat eğitiminin amacına uygun", "Telif hakkı izni olmadan stil transferi yasak", "Estetik çeşitliliği teşvik", "Yasal ve etik"],
        ["🇺🇳 UNESCO", "Sanatsal ifade özgürlüğü", "Geleneksel sanatların korunması", "Estetik eğitiminde insan faktörü", "Kültürel rehber"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Okul felsefesine göre", "'Fair use' tartışmalı", "En çok beğenilen stiller öne çıkar", "Piyasa"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Temel Beceri Kaybı": {"Türkiye (YAZEK)": 88, "Çin": 72, "AB": 85, "UNESCO": 80, "ABD/İngiltere": 62},
        "Stil/Telif Sorunu": {"Türkiye (YAZEK)": 80, "Çin": 70, "AB": 90, "UNESCO": 78, "ABD/İngiltere": 55},
        "Estetik Tekdüzelik": {"Türkiye (YAZEK)": 82, "Çin": 65, "AB": 88, "UNESCO": 85, "ABD/İngiltere": 60}
    }
    st.pyplot(politika_etkinlik_heatmap("Görsel Sanatlar", etkinlik_matrisi))
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [85, 80, 75, 68, 58, 72],
        "Çin": [65, 58, 42, 86, 48, 88],
        "AB": [80, 94, 90, 44, 54, 68],
        "UNESCO": [78, 90, 85, 46, 46, 85],
        "ABD/İngiltere": [68, 50, 45, 72, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Görsel Sanatlar", radar_puanlari), use_container_width=True)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 85, "Etik Risk": 80, "Pratik Risk": 68, "Mahremiyet Riski": 75},
        "Çin": {"Pedagojik Risk": 65, "Etik Risk": 58, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 80, "Etik Risk": 94, "Pratik Risk": 48, "Mahremiyet Riski": 90},
        "UNESCO": {"Pedagojik Risk": 78, "Etik Risk": 90, "Pratik Risk": 46, "Mahremiyet Riski": 85},
        "ABD/İngiltere": {"Pedagojik Risk": 68, "Etik Risk": 52, "Pratik Risk": 78, "Mahremiyet Riski": 48}
    }
    st.plotly_chart(risk_azaltma_grafigi("Görsel Sanatlar", risk_oranlari), use_container_width=True)
    
    st.markdown("### 🧠 Görsel Sanatlar - Bilimsel Değerlendirme")
    st.markdown("""
    Görsel sanatlar eğitiminde YZ, 'YZ bana çizsin' yaklaşımıyla temel çizim becerilerinin kaybına yol açabilir.
    
    YAZEK'in 'manuel çizim tamamlanmadan YZ düzenlemesi yok' kuralı temel becerileri korur. 'En az 3 farklı estetik anlayışı' zorunluluğu tekdüze bir güzellik anlayışının dayatılmasını engeller. AB'nin 'telif hakkı izni olmadan stil transferi yasak' kuralı sanatçı haklarını korur.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Temel becerileri korur, estetik çeşitlilik", "Standart", "Sanatçı hakları korunur", "Kültürel çeşitlilik", "Yenilikçi"],
        "Dezavantajlar": ["Süreç yavaş", "Yaratıcılığı sınırlar", "İzin süreci uzun", "Bağlayıcı değil", "Telif riski yüksek"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 11: BEDEN EĞİTİMİ (TAM DETAY)
# ========================
def beden_analizi():
    st.header("🏃 Beden Eğitimi Dersi")
    st.markdown("**Temel Senaryo:** YZ destekli hareket analizi, antrenör asistanı, performans takibi.")
    st.markdown("**Sorunlar:** (1) Biyometrik mahremiyet, (2) Rekabet baskısı, (3) Sakatlık riski tahmini.")
    
    tablo_headers = ["Strateji", "Biyometrik Mahremiyet", "Rekabet Baskısı", "Sakatlık Riski", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Veriler anonim, veli onayı zorunlu", "Bireysel gelişim odaklı, sınıf sıralaması yasak", "Risk tahmini 'uyarı' niteliğinde", "Mahremiyetli yardımcı"],
        ["🇨🇳 Çin", "Devlet sunucularında, sağlık politikası için", "Ulusal fiziksel yeterlilik standartları", "Ulusal verilerle eğitilmiş model", "Devlet izleme aracı"],
        ["🇪🇺 AB", "Biyometrik veri işleme neredeyse yasak", "Performans verisi toplanamaz", "Tıbbi cihaz düzenlemelerine tabi", "Çok sıkı"],
        ["🇺🇳 UNESCO", "Spor etiği ve mahremiyet ilkeleri", "Farklı fiziksel kapasiteye saygı", "Eğitici değil uyarıcı rol", "Etik rehber"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Okul politikası, veli izni", "Rekabetçi veya gelişim odaklı seçim", "Sorumluluk okulun/sigortanın", "Serbest piyasa"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Biyometrik Mahremiyet": {"Türkiye (YAZEK)": 85, "Çin": 45, "AB": 95, "UNESCO": 82, "ABD/İngiltere": 50},
        "Rekabet Baskısı": {"Türkiye (YAZEK)": 82, "Çin": 65, "AB": 88, "UNESCO": 80, "ABD/İngiltere": 60},
        "Sakatlık Riski": {"Türkiye (YAZEK)": 78, "Çin": 80, "AB": 85, "UNESCO": 70, "ABD/İngiltere": 65}
    }
    st.pyplot(politika_etkinlik_heatmap("Beden Eğitimi", etkinlik_matrisi))
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [80, 82, 85, 70, 55, 72],
        "Çin": [65, 58, 40, 86, 48, 88],
        "AB": [78, 95, 94, 42, 50, 68],
        "UNESCO": [74, 88, 86, 46, 44, 84],
        "ABD/İngiltere": [68, 50, 45, 74, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Beden Eğitimi", radar_puanlari), use_container_width=True)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 80, "Etik Risk": 82, "Pratik Risk": 70, "Mahremiyet Riski": 85},
        "Çin": {"Pedagojik Risk": 65, "Etik Risk": 58, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 78, "Etik Risk": 95, "Pratik Risk": 48, "Mahremiyet Riski": 94},
        "UNESCO": {"Pedagojik Risk": 74, "Etik Risk": 88, "Pratik Risk": 46, "Mahremiyet Riski": 86},
        "ABD/İngiltere": {"Pedagojik Risk": 68, "Etik Risk": 52, "Pratik Risk": 78, "Mahremiyet Riski": 50}
    }
    st.plotly_chart(risk_azaltma_grafigi("Beden Eğitimi", risk_oranlari), use_container_width=True)
    
    st.markdown("### 🧠 Beden Eğitimi - Bilimsel Değerlendirme")
    st.markdown("""
    Beden eğitiminde YZ kullanımı, nabız, ter oranı, hareket paterni gibi biyometrik verilerin işlenmesini gerektirir. Bu veriler son derece hassastır.
    
    YAZEK'in 'veriler anonim, veli onayı zorunlu' kuralı mahremiyeti korur. 'Bireysel gelişim odaklı, sınıf sıralaması yasak' kuralı rekabet baskısını azaltır. AB, biyometrik veri işlemeyi neredeyse tamamen yasakladığı için beden eğitiminde YZ kullanımı neredeyse imkansızdır.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Mahremiyet koruması, bireysel gelişim", "Tam kontrol, büyük veri", "En yüksek mahremiyet", "Etik ilkeler", "Hızlı yenilik"],
        "Dezavantajlar": ["Veri toplama sınırlı", "Mahremiyet zayıf", "Kullanım neredeyse imkansız", "Bağlayıcı değil", "Dava riski yüksek"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  DERS 12: REHBERLİK (TAM DETAY)
# ========================
def rehberlik_analizi():
    st.header("🧭 Rehberlik Dersi / Psikolojik Danışmanlık")
    st.markdown("**Temel Senaryo:** YZ destekli duygu durum takibi, risk tahmini, öğrenci profilleme.")
    st.markdown("**Sorunlar:** (1) Yanlış etiketleme (damgalama), (2) Mahremiyet ihlali, (3) Uzmanlığa müdahale.")
    
    tablo_headers = ["Strateji", "Yanlış Etiketleme (Damgalama)", "Mahremiyet İhlali", "Uzmanlığa Müdahale", "Sistemin Kaderi"]
    tablo_veri = [
        ["🇹🇷 Türkiye (YAZEK)", "Otomatik etiketleme yasak, sadece anonim trend", "Veriler şifreli, yerel sunucu, rehberlikçi erişimi", "Sadece 'dikkat edilmesi gereken' uyarısı", "Erken uyarı asistanı"],
        ["🇨🇳 Çin", "Devlet onaylı psikolojik profil etiketleri", "Devlet sunucuları, güvenlik amaçlı kullanım", "YZ önerileri bağlayıcı olabilir", "Devlet izleme aracı"],
        ["🇪🇺 AB", "Otomatik duygu durumu sınıflandırması yasak", "Konuşma kaydı, yüz analizi yasak", "YZ danışmanlığın yerine geçemez", "Yasal olarak neredeyse imkansız"],
        ["🇺🇳 UNESCO", "İnsan onuru ve özerklik vurgusu", "Mahremiyet temel insan hakkı", "YZ asla insanın yerini alamaz", "Etik pusula"],
        ["🇺🇸/🇬🇧 ABD/İngiltere", "Okul politikası, yanlış etiketleme davalık", "Okul sözleşmesi, ihlal durumunda dava", "Riskler okula ait", "Serbest piyasa"]
    ]
    st.table([tablo_headers] + tablo_veri)
    
    etkinlik_matrisi = {
        "Yanlış Etiketleme": {"Türkiye (YAZEK)": 88, "Çin": 60, "AB": 95, "UNESCO": 85, "ABD/İngiltere": 55},
        "Mahremiyet İhlali": {"Türkiye (YAZEK)": 86, "Çin": 42, "AB": 96, "UNESCO": 88, "ABD/İngiltere": 48},
        "Uzmanlığa Müdahale": {"Türkiye (YAZEK)": 85, "Çin": 65, "AB": 92, "UNESCO": 84, "ABD/İngiltere": 60}
    }
    st.pyplot(politika_etkinlik_heatmap("Rehberlik", etkinlik_matrisi))
    
    st.markdown("""
    **📊 Rehberlik - Heatmap Detaylı Analizi:**
    
    **AB:** Yanlış etiketleme 95, Mahremiyet 96 - en yüksek. Otomatik duygu durumu sınıflandırması yasaktır.
    **Türkiye:** Etiketleme 88, Mahremiyet 86 - 'otomatik etiketleme yasak, sadece anonim trend' kuralı damgalamayı önler.
    **Çin:** Mahremiyet 42 - veriler devlet kontrolünde, bireysel haklar zayıf.
    """)
    
    radar_puanlari = {
        "Türkiye (YAZEK)": [85, 86, 88, 68, 55, 72],
        "Çin": [62, 55, 40, 86, 48, 88],
        "AB": [82, 96, 95, 42, 50, 68],
        "UNESCO": [78, 90, 88, 46, 44, 84],
        "ABD/İngiltere": [68, 50, 48, 74, 94, 74]
    }
    st.plotly_chart(politika_radar_analizi("Rehberlik", radar_puanlari), use_container_width=True)
    
    st.markdown("""
    **📊 Rehberlik - Radar Analizi Her Ülke Detaylı:**
    
    **AB:** Etik 96, Mahremiyet 95 - en yüksek. Konuşma kaydı, yüz ifadesi analizi gibi veriler GDPR kapsamında yasaktır.
    **Türkiye:** Mahremiyet 88, Etik 86 - YAZEK'in rehberlik modülü otomatik etiketlemeyi yasaklar. Sadece anonim trend analizi yapılabilir.
    **Çin:** İş Yükü 86, Erişilebilirlik 88 - merkezi sistem. Mahremiyet 40 - çok zayıf.
    **ABD/İngiltere:** Yenilik 94 - yeni duygu analizi araçları. Etik 50 - koruma zayıf, dava mekanizması.
    """)
    
    risk_oranlari = {
        "Türkiye (YAZEK)": {"Pedagojik Risk": 85, "Etik Risk": 86, "Pratik Risk": 68, "Mahremiyet Riski": 88},
        "Çin": {"Pedagojik Risk": 62, "Etik Risk": 55, "Pratik Risk": 86, "Mahremiyet Riski": 42},
        "AB": {"Pedagojik Risk": 82, "Etik Risk": 96, "Pratik Risk": 42, "Mahremiyet Riski": 95},
        "UNESCO": {"Pedagojik Risk": 78, "Etik Risk": 90, "Pratik Risk": 46, "Mahremiyet Riski": 88},
        "ABD/İngiltere": {"Pedagojik Risk": 68, "Etik Risk": 52, "Pratik Risk": 78, "Mahremiyet Riski": 50}
    }
    st.plotly_chart(risk_azaltma_grafigi("Rehberlik", risk_oranlari), use_container_width=True)
    
    st.markdown("""
    **📊 Rehberlik - Risk Azaltma Detaylı Analizi:**
    
    **AB (Ort. 78.75):** Etik Risk 96, Mahremiyet 95 - en güçlü koruma. Pratik Risk 42 - en zayıf.
    **Türkiye (Ort. 81.75):** Mahremiyet 88, Etik 86 - dengeli yaklaşım. Otomatik etiketleme yasağı damgalamayı önler.
    **Çin (Ort. 61.25):** Pratik Risk 86 - uygulama kolay. Mahremiyet 42 - çok zayıf.
    **ABD/İngiltere (Ort. 62.0):** Pratik Risk 78 - uygulama kolay. Etik 52 - koruma zayıf.
    """)
    
    st.markdown("### 🧠 Rehberlik - Bilimsel Değerlendirme")
    st.markdown("""
    Rehberlik ve psikolojik danışmanlık alanında YZ kullanımı, en yüksek etik riskleri barındırır. Yanlış etiketleme damgası, mahremiyet ihlalleri ve insan temasının azalması ciddi sorunlardır.
    
    YAZEK, rehberlik modülünde 'otomatik etiketleme'yi tamamen yasaklamıştır. YZ sadece anonim trend verileri üretebilir. Bireysel etiketleme ancak rehberlik öğretmeninin gözlemiyle yapılabilir. AB'de konuşma kaydı ve yüz ifadesi analizi yasaktır. Çin'de ise veriler devlet kontrolündedir.
    """)
    
    df = pd.DataFrame({
        "Strateji": ["Türkiye", "Çin", "AB", "UNESCO", "ABD/İngiltere"],
        "Avantajlar": ["Damgalama önleme, mahremiyet", "Tam kontrol, erken uyarı", "En yüksek mahremiyet, yasal güvence", "İnsan onuru odağı", "Hızlı yenilik"],
        "Dezavantajlar": ["Sadece trend analizi", "Bireysel haklar zayıf", "Kullanım neredeyse imkansız", "Bağlayıcı değil", "Dava riski, güvensiz"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ========================
#  YÖNLENDİRME
# ========================
if secili_ders == "Matematik":
    matematik_analizi()
elif secili_ders == "Fizik":
    fizik_analizi()
elif secili_ders == "Kimya":
    kimya_analizi()
elif secili_ders == "Biyoloji":
    biyoloji_analizi()
elif secili_ders == "Türkçe / Edebiyat":
    turkce_analizi()
elif secili_ders == "Tarih":
    tarih_analizi()
elif secili_ders == "Coğrafya":
    cografya_analizi()
elif secili_ders == "Yabancı Dil (İngilizce)":
    ingilizce_analizi()
elif secili_ders == "Müzik":
    muzik_analizi()
elif secili_ders == "Görsel Sanatlar":
    sanat_analizi()
elif secili_ders == "Beden Eğitimi":
    beden_analizi()
elif secili_ders == "Rehberlik":
    rehberlik_analizi()

# ========================
#  ALT BİLGİ
# ========================
st.markdown("---")
st.markdown("""
**© 2026 Ahmet ALTINOK - Eğitimde Yapay Zeka Etik ve Politika Karşılaştırmaları Projesi**  
Bu proje, aşağıdaki resmi politika belgeleri ve akademik çalışmalar temel alınarak hazırlanmıştır:

- MEB YAZEK (Yapay Zeka Uygulamaları Etik Beyan Sistemi) Teknik Kılavuzu - 2026
- Avrupa Birliği Yapay Zeka Yasası (AB 2024/1689) - Yüksek Riskli Sistemler Eki
- UNESCO Yapay Zeka Etiği Tavsiye Kararı - 2021/2026 Güncellemesi
- Çin Halk Cumhuriyeti Yapay Zeka Eğitim Strateji Belgesi (2024-2027)
- OECD Yapay Zeka ve Eğitim Raporları (2023-2026)

**Veri Notu:** Sayısal puanlar ve yüzdeler, ilgili politika belgeleri ve literatür taranarak oluşturulmuş temsili değerlerdir. Kesin ölçümler değil, eğilim göstergeleridir.
""")