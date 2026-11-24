from flask import Flask, render_template_string, request

app = Flask(__name__)

TRANSLATIONS = {
    "pl": {
        "title": "Kalkulator Wypłaty Dania 2026 – Policz Netto (Lønseddel)",
        "header_title": "🇩🇰 Kalkulator Wypłaty Dania",
        "header_sub": "Sprawdź swoją wypłatę na rękę (netto) i zweryfikuj duński pasek (lønseddel)",
        "ad_top": "[Miejsce na reklamę Google AdSense – Baner Górny 728x90 / Responsywny]",
        "ad_bottom": "[Miejsce na reklamę Google AdSense – Baner Dolny / Artykułowy]",
        "quick_period": "Szybki wybór okresu rozliczeniowego:",
        "btn_14d": "2 tygodnie (74h + ATP 49.50)",
        "btn_month": "Miesiąc (160.33h + ATP 99.00)",
        "sec_1": "1. Godziny i stawka podstawowa",
        "hours": "Liczba godzin zwykłych",
        "hours_hint": "Np. 160.33 (miesiąc) lub 74 (2 tyg.)",
        "rate": "Stawka godzinowa (DKK brutto)",
        "rate_hint": "Twoja podstawowa stawka z umowy",
        "sec_2": "2. Nadgodziny, chorobowe i dodatki",
        "ot_hours": "Nadgodziny (liczba godzin)",
        "ot_hours_hint": "Godziny ponad normę",
        "ot_rate": "Stawka za nadgodziny (DKK)",
        "ot_rate_hint": "Pełna stawka (np. 150% = stawka x 1.5)",
        "sick_hours": "Godziny chorobowe (Sygeløn)",
        "sick_hours_hint": "Godziny na L4 (bez naliczania Feriepenge)",
        "sick_rate": "Stawka za chorobowe (DKK)",
        "sick_rate_hint": "Zwykle ~131 DKK (Sygedagpenge) lub 100% stawki",
        "bonus": "Inne dodatki brutto (DKK)",
        "bonus_hint": "Nocki, chłodnia, dodatek zmianowy, premia",
        "fritvalg_pct": "Konto Fritvalgskonto (%)",
        "fritvalg_hint": "Dodatek odkładany przez firmę (zwykle 9% lub 0%)",
        "sec_3": "3. Podatki SKAT, emerytura i potrącenia",
        "fradrag": "Kwota wolna – Fradrag (DKK)",
        "fradrag_hint": "Kwota z paska dla danego okresu",
        "tax_pct": "Procent podatku – Trækprocent (%)",
        "tax_pct_hint": "Zwykle 36% – 42% (z karty podatkowej)",
        "pension_pct": "Składka emerytalna – Pension (%)",
        "pension_pct_hint": "Twój wkład własny (zwykle 0%, 2% lub 4%)",
        "atp": "Składka emerytalna ATP (DKK)",
        "atp_hint": "Stała kwota: ~99 DKK/mies. lub ~49.50 DKK/2 tyg.",
        "other_ded": "Inne potrącenia po podatku (DKK)",
        "other_ded_hint": "Np. mieszkanie firmowe, dojazdy, związki",
        "feriepenge": "Naliczaj <strong>Feriepenge (12,5%)</strong> od wynagrodzenia (standard dla pracowników godzinowych)",
        "pln_rate": "Kurs wymiany DKK → PLN (do podglądu w złotówkach)",
        "btn_calc": "Oblicz moją wypłatę netto",
        "res_netto_label": "Szacowana wypłata na rękę (Udbetalt):",
        "res_pln_info": "przy kursie",
        "res_breakdown": "Szczegółowe rozliczenie (jak na Lønseddel):",
        "row_base": "Wynagrodzenie podstawowe",
        "row_ot": "Nadgodziny",
        "row_sick": "Wynagrodzenie chorobowe (Sygeløn)",
        "row_bonus": "Dodatki (nocki / zmiany / premie)",
        "row_gross": "Suma wynagrodzenia brutto (Bruttoløn)",
        "row_fp_gross": "+ Odłożono na Feriepenge (12,5% na konto urlopowe)",
        "row_fv_gross": "+ Odłożono na Fritvalgskonto",
        "row_pension": "- Składka emerytalna pracownika (Pension)",
        "row_atp": "- Składka emerytalna ATP (ATP-bidrag)",
        "row_am": "- Podatek AM-bidrag (8%)",
        "row_taxable": "Podstawa opodatkowania (po odjęciu Fradrag)",
        "row_askat": "- Podatek dochodowy A-skat",
        "row_fp_tax": "- Podatek potrącony z góry za Feriepenge",
        "row_other_ded": "- Inne potrącenia po podatku (mieszkanie / inne)",
        "unit_h": "godz.",
        "aff_title": "💸 Wysyłasz wypłatę do Polski? Nie trać na kursie banku!",
        "aff_desc": "Duńskie banki pobierają nawet 3–4% ukrytej marży za przewalutowanie. Sprawdź przelew po kursie międzybankowym.",
        "aff_btn": "Sprawdź darmowy przelew DKK → PLN",
        "aff_alert": "Tutaj wstawisz swój link polecający do Wise lub Revolut!",
        "footer": "Kalkulator ma charakter poglądowy. Wyniki mogą się nieznacznie różnić w zależności od indywidualnych zapisów na pasku (Lønseddel)."
    },
    "en": {
        "title": "Denmark Salary Calculator 2026 – Net Pay (Lønseddel)",
        "header_title": "🇩🇰 Denmark Salary Calculator",
        "header_sub": "Quickly calculate your net take-home pay and verify your Danish payslip (lønseddel)",
        "ad_top": "[Google AdSense Ad Slot – Top Banner 728x90 / Responsive]",
        "ad_bottom": "[Google AdSense Ad Slot – Bottom / In-Article Banner]",
        "quick_period": "Quick pay period preset:",
        "btn_14d": "Bi-weekly (74h + ATP 49.50)",
        "btn_month": "Monthly (160.33h + ATP 99.00)",
        "sec_1": "1. Regular Hours & Base Rate",
        "hours": "Regular working hours",
        "hours_hint": "E.g. 160.33 (monthly) or 74 (bi-weekly)",
        "rate": "Hourly wage (DKK gross)",
        "rate_hint": "Your base hourly rate from contract",
        "sec_2": "2. Overtime, Sick Pay & Allowances",
        "ot_hours": "Overtime hours",
        "ot_hours_hint": "Extra hours worked",
        "ot_rate": "Overtime hourly rate (DKK)",
        "ot_rate_hint": "Full rate (e.g. 150% = base rate x 1.5)",
        "sick_hours": "Sick leave hours (Sygeløn)",
        "sick_hours_hint": "Sick hours (excluded from standard Feriepenge)",
        "sick_rate": "Sick pay hourly rate (DKK)",
        "sick_rate_hint": "Usually ~131 DKK (Sygedagpenge) or 100% rate",
        "bonus": "Other gross allowances (DKK)",
        "bonus_hint": "Night shifts, cold storage, shift bonus",
        "fritvalg_pct": "Fritvalgskonto savings (%)",
        "fritvalg_hint": "Employer-funded flexible account (usually 9% or 0%)",
        "sec_3": "3. SKAT Taxes, Pension & Deductions",
        "fradrag": "Tax-free allowance – Fradrag (DKK)",
        "fradrag_hint": "Deduction amount shown on your payslip",
        "tax_pct": "Tax rate – Trækprocent (%)",
        "tax_pct_hint": "Usually 36% – 42% (from your tax card)",
        "pension_pct": "Employee pension contribution (%)",
        "pension_pct_hint": "Your own share (usually 0%, 2% or 4%)",
        "atp": "ATP Pension contribution (DKK)",
        "atp_hint": "Fixed fee: ~99 DKK/month or ~49.50 DKK/2 weeks",
        "other_ded": "Other post-tax deductions (DKK)",
        "other_ded_hint": "E.g. company housing, transport, union fees",
        "feriepenge": "Calculate <strong>Feriepenge (12.5%)</strong> holiday pay (standard for hourly workers)",
        "pln_rate": "Exchange rate DKK → EUR / PLN (optional preview)",
        "btn_calc": "Calculate My Net Salary",
        "res_netto_label": "Estimated Net Payout (Udbetalt):",
        "res_pln_info": "at rate",
        "res_breakdown": "Detailed Payslip Breakdown (Lønseddel):",
        "row_base": "Base salary",
        "row_ot": "Overtime pay",
        "row_sick": "Sick pay (Sygeløn)",
        "row_bonus": "Allowances (night / shift / bonuses)",
        "row_gross": "Total Gross Salary (Bruttoløn)",
        "row_fp_gross": "+ Accrued Feriepenge (12.5% holiday account)",
        "row_fv_gross": "+ Accrued Fritvalgskonto",
        "row_pension": "- Employee Pension contribution",
        "row_atp": "- ATP Pension (ATP-bidrag)",
        "row_am": "- AM-bidrag tax (8%)",
        "row_taxable": "Taxable income (after Fradrag)",
        "row_askat": "- Income tax A-skat",
        "row_fp_tax": "- Pre-deducted tax on Feriepenge",
        "row_other_ded": "- Other post-tax deductions (housing / other)",
        "unit_h": "hrs",
        "aff_title": "💸 Sending money abroad from Denmark? Don't lose on bank fees!",
        "aff_desc": "Danish banks charge up to 3–4% in hidden exchange markups. Check real mid-market transfers.",
        "aff_btn": "Check Low-Cost International Transfer",
        "aff_alert": "Insert your Wise or Revolut affiliate link here!",
        "footer": "This calculator provides an estimate. Actual payout may vary slightly depending on specific payslip agreements."
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ t.title }}</title>
    <style>
        :root {
            --primary: #c8102e;
            --primary-dark: #9e0b23;
            --bg: #f4f6f9;
            --card: #ffffff;
            --text: #1f2937;
            --muted: #6b7280;
            --border: #e5e7eb;
            --green: #059669;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }
        body { background: var(--bg); color: var(--text); line-height: 1.5; padding: 15px; }
        .container { max-width: 700px; margin: 0 auto; }
        
        /* Pasek języka */
        .top-bar { display: flex; justify-content: flex-end; gap: 8px; margin-bottom: 8px; }
        .lang-btn {
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            padding: 6px 12px;
            border-radius: 20px;
            background: #e5e7eb;
            color: #374151;
            transition: all 0.2s;
        }
        .lang-btn.active {
            background: var(--primary);
            color: #ffffff;
        }

        header { text-align: center; margin-bottom: 18px; padding: 8px 10px; }
        header h1 { font-size: 1.65rem; color: var(--primary); margin-bottom: 5px; }
        header p { color: var(--muted); font-size: 0.95rem; }
        
        .ad-slot {
            background: #e9ecef;
            border: 1px dashed #adb5bd;
            color: #6c757d;
            text-align: center;
            padding: 16px 10px;
            border-radius: 8px;
            margin-bottom: 18px;
            font-size: 0.82rem;
        }

        .card {
            background: var(--card);
            border-radius: 12px;
            padding: 22px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }

        /* Szybkie przyciski okresu */
        .preset-box {
            background: #f8fafc;
            border: 1px solid var(--border);
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 18px;
            text-align: center;
        }
        .preset-box span { display: block; font-size: 0.82rem; color: var(--muted); margin-bottom: 8px; font-weight: 600; }
        .preset-btns { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
        .btn-preset {
            background: #ffffff;
            border: 1px solid #cbd5e1;
            padding: 7px 12px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 600;
            color: #334155;
            cursor: pointer;
        }
        .btn-preset:hover { border-color: var(--primary); color: var(--primary); }

        .section-title {
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 14px;
            padding-bottom: 6px;
            border-bottom: 2px solid var(--bg);
            color: #111827;
        }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
        @media (max-width: 540px) { .grid { grid-template-columns: 1fr; } }
        
        .form-group { margin-bottom: 12px; }
        label { display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 4px; color: #374151; }
        .hint { font-size: 0.77rem; color: var(--muted); font-weight: 400; display: block; }
        input {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 1rem;
            background: #fafafa;
        }
        input:focus {
            outline: none;
            border-color: var(--primary);
            background: #fff;
        }
        .checkbox-group {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 12px 0;
            background: #f9fafb;
            padding: 10px 12px;
            border-radius: 8px;
            border: 1px solid var(--border);
        }
        .checkbox-group input { width: 18px; height: 18px; accent-color: var(--primary); }
        .checkbox-group label { margin: 0; cursor: pointer; }

        button.btn-calc {
            width: 100%;
            background: var(--primary);
            color: white;
            border: none;
            padding: 14px;
            font-size: 1.05rem;
            font-weight: 700;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 10px;
            transition: background 0.2s;
        }
        button.btn-calc:hover { background: var(--primary-dark); }

        .result-box { border-left: 5px solid var(--green); }
        .netto-highlight {
            background: #ecfdf5;
            padding: 16px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 18px;
        }
        .netto-highlight span { display: block; font-size: 0.9rem; color: #065f46; font-weight: 600; }
        .netto-highlight strong { font-size: 2rem; color: var(--green); }
        .netto-pln { font-size: 0.95rem; color: #047857; margin-top: 4px; }

        table { width: 100%; border-collapse: collapse; font-size: 0.91rem; }
        td { padding: 9px 4px; border-bottom: 1px solid var(--border); }
        td:last-child { text-align: right; font-weight: 600; }
        tr.deduction td:last-child { color: #dc2626; }
        tr.addition td:last-child { color: var(--green); }

        .affiliate-box {
            background: linear-gradient(135deg, #1e293b, #0f172a);
            color: white;
            padding: 18px;
            border-radius: 10px;
            margin-top: 18px;
            text-align: center;
        }
        .affiliate-box h3 { font-size: 1rem; margin-bottom: 6px; }
        .affiliate-box p { font-size: 0.85rem; color: #cbd5e1; margin-bottom: 12px; }
        .btn-aff {
            display: inline-block;
            background: #38bdf8;
            color: #0f172a;
            font-weight: 700;
            text-decoration: none;
            padding: 10px 18px;
            border-radius: 6px;
            font-size: 0.9rem;
        }
        footer { text-align: center; font-size: 0.8rem; color: var(--muted); margin-top: 25px; padding-bottom: 20px; }
    </style>
</head>
<body>
<div class="container">
    <div class="top-bar">
        <a href="/?lang=pl" class="lang-btn {% if lang == 'pl' %}active{% endif %}">🇵🇱 Polski</a>
        <a href="/?lang=en" class="lang-btn {% if lang == 'en' %}active{% endif %}">🇬🇧 English</a>
    </div>

    <header>
        <h1>{{ t.header_title }}</h1>
        <p>{{ t.header_sub }}</p>
    </header>

    <div class="ad-slot">{{ t.ad_top }}</div>

    <div class="card">
        <div class="preset-box">
            <span>{{ t.quick_period }}</span>
            <div class="preset-btns">
                <button type="button" class="btn-preset" onclick="setPreset(74, 49.50, 2200)">{{ t.btn_14d }}</button>
                <button type="button" class="btn-preset" onclick="setPreset(160.33, 99.00, 4600)">{{ t.btn_month }}</button>
            </div>
        </div>

        <form method="POST" action="/?lang={{ lang }}">
            <div class="section-title">{{ t.sec_1 }}</div>
            <div class="grid">
                <div class="form-group">
                    <label>{{ t.hours }}
                        <span class="hint">{{ t.hours_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="hours" name="hours" value="{{ form.hours }}" required>
                </div>
                <div class="form-group">
                    <label>{{ t.rate }}
                        <span class="hint">{{ t.rate_hint }}</span>
                    </label>
                    <input type="number" step="0.01" name="rate" value="{{ form.rate }}" required>
                </div>
            </div>

            <div class="section-title" style="margin-top: 14px;">{{ t.sec_2 }}</div>
            <div class="grid">
                <div class="form-group">
                    <label>{{ t.ot_hours }}
                        <span class="hint">{{ t.ot_hours_hint }}</span>
                    </label>
                    <input type="number" step="0.01" name="ot_hours" value="{{ form.ot_hours }}">
                </div>
                <div class="form-group">
                    <label>{{ t.ot_rate }}
                        <span class="hint">{{ t.ot_rate_hint }}</span>
                    </label>
                    <input type="number" step="0.01" name="ot_rate" value="{{ form.ot_rate }}">
                </div>
                <div class="form-group">
                    <label>{{ t.sick_hours }}
                        <span class="hint">{{ t.sick_hours_hint }}</span>
                    </label>
                    <input type="number" step="0.01" name="sick_hours" value="{{ form.sick_hours }}">
                </div>
                <div class="form-group">
                    <label>{{ t.sick_rate }}
                        <span class="hint">{{ t.sick_rate_hint }}</span>
                    </label>
                    <input type="number" step="0.01" name="sick_rate" value="{{ form.sick_rate }}">
                </div>
                <div class="form-group">
                    <label>{{ t.bonus }}
                        <span class="hint">{{ t.bonus_hint }}</span>
                    </label>
                    <input type="number" step="0.01" name="bonus" value="{{ form.bonus }}">
                </div>
                <div class="form-group">
                    <label>{{ t.fritvalg_pct }}
                        <span class="hint">{{ t.fritvalg_hint }}</span>
                    </label>
                    <input type="number" step="0.1" name="fritvalg_pct" value="{{ form.fritvalg_pct }}">
                </div>
            </div>

            <div class="section-title" style="margin-top: 14px;">{{ t.sec_3 }}</div>
            <div class="grid">
                <div class="form-group">
                    <label>{{ t.fradrag }}
                        <span class="hint">{{ t.fradrag_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="fradrag" name="fradrag" value="{{ form.fradrag }}" required>
                </div>
                <div class="form-group">
                    <label>{{ t.tax_pct }}
                        <span class="hint">{{ t.tax_pct_hint }}</span>
                    </label>
                    <input type="number" step="0.1" name="tax_pct" value="{{ form.tax_pct }}" required>
                </div>
                <div class="form-group">
                    <label>{{ t.pension_pct }}
                        <span class="hint">{{ t.pension_pct_hint }}</span>
                    </label>
                    <input type="number" step="0.1" name="pension_pct" value="{{ form.pension_pct }}">
                </div>
                <div class="form-group">
                    <label>{{ t.atp }}
                        <span class="hint">{{ t.atp_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="atp" name="atp" value="{{ form.atp }}">
                </div>
            </div>

            <div class="form-group">
                <label>{{ t.other_ded }}
                    <span class="hint">{{ t.other_ded_hint }}</span>
                </label>
                <input type="number" step="0.01" name="other_ded" value="{{ form.other_ded }}">
            </div>

            <div class="checkbox-group">
                <input type="checkbox" id="feriepenge" name="feriepenge" {% if form.feriepenge %}checked{% endif %}>
                <label for="feriepenge">{{ t.feriepenge|safe }}</label>
            </div>

            <div class="form-group">
                <label>{{ t.pln_rate }}</label>
                <input type="number" step="0.01" name="pln_rate" value="{{ form.pln_rate }}">
            </div>

            <button type="submit" class="btn-calc">{{ t.btn_calc }}</button>
        </form>
    </div>

    {% if result %}
    <div class="card result-box">
        <div class="netto-highlight">
            <span>{{ t.res_netto_label }}</span>
            <strong>{{ "%.2f"|format(result.netto) }} DKK</strong>
            <div class="netto-pln">≈ {{ "%.2f"|format(result.netto_pln) }} PLN ({{ t.res_pln_info }} {{ form.pln_rate }})</div>
        </div>

        <div class="section-title">{{ t.res_breakdown }}</div>
        <table>
            <tr>
                <td>{{ t.row_base }} ({{ form.hours }} {{ t.unit_h }})</td>
                <td>{{ "%.2f"|format(result.base_gross) }} DKK</td>
            </tr>
            {% if result.ot_gross > 0 %}
            <tr>
                <td>{{ t.row_ot }} ({{ form.ot_hours }} {{ t.unit_h }})</td>
                <td>{{ "%.2f"|format(result.ot_gross) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.sick_gross > 0 %}
            <tr>
                <td>{{ t.row_sick }} ({{ form.sick_hours }} {{ t.unit_h }})</td>
                <td>{{ "%.2f"|format(result.sick_gross) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.bonus > 0 %}
            <tr>
                <td>{{ t.row_bonus }}</td>
                <td>{{ "%.2f"|format(result.bonus) }} DKK</td>
            </tr>
            {% endif %}
            <tr>
                <td><strong>{{ t.row_gross }}</strong></td>
                <td><strong>{{ "%.2f"|format(result.total_gross) }} DKK</strong></td>
            </tr>
            {% if result.feriepenge_gross > 0 %}
            <tr class="addition">
                <td>{{ t.row_fp_gross }}</td>
                <td>{{ "%.2f"|format(result.feriepenge_gross) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.fritvalg_gross > 0 %}
            <tr class="addition">
                <td>{{ t.row_fv_gross }} ({{ form.fritvalg_pct }}%)</td>
                <td>{{ "%.2f"|format(result.fritvalg_gross) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.pension > 0 %}
            <tr class="deduction">
                <td>{{ t.row_pension }} ({{ form.pension_pct }}%)</td>
                <td>-{{ "%.2f"|format(result.pension) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.atp > 0 %}
            <tr class="deduction">
                <td>{{ t.row_atp }}</td>
                <td>-{{ "%.2f"|format(result.atp) }} DKK</td>
            </tr>
            {% endif %}
            <tr class="deduction">
                <td>{{ t.row_am }}</td>
                <td>-{{ "%.2f"|format(result.am_bidrag) }} DKK</td>
            </tr>
            <tr>
                <td>{{ t.row_taxable }} ({{ form.fradrag }} DKK)</td>
                <td>{{ "%.2f"|format(result.taxable_income) }} DKK</td>
            </tr>
            <tr class="deduction">
                <td>{{ t.row_askat }} ({{ form.tax_pct }}%)</td>
                <td>-{{ "%.2f"|format(result.a_skat) }} DKK</td>
            </tr>
            {% if result.feriepenge_tax > 0 %}
            <tr class="deduction">
                <td>{{ t.row_fp_tax }}</td>
                <td>-{{ "%.2f"|format(result.feriepenge_tax) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.other_ded > 0 %}
            <tr class="deduction">
                <td>{{ t.row_other_ded }}</td>
                <td>-{{ "%.2f"|format(result.other_ded) }} DKK</td>
            </tr>
            {% endif %}
        </table>

        <div class="affiliate-box">
            <h3>{{ t.aff_title }}</h3>
            <p>{{ t.aff_desc }}</p>
            <a href="#" class="btn-aff" onclick="alert('{{ t.aff_alert }}')">{{ t.aff_btn }}</a>
        </div>
    </div>
    {% endif %}

    <div class="ad-slot">{{ t.ad_bottom }}</div>

    <footer>{{ t.footer }}</footer>
</div>

<script>
function setPreset(hours, atp, fradrag) {
    document.getElementById('hours').value = hours;
    document.getElementById('atp').value = atp.toFixed(2);
    document.getElementById('fradrag').value = fradrag;
}
</script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    lang = request.args.get("lang")
    if lang not in ("pl", "en"):
        accept_lang = request.headers.get("Accept-Language", "")
        lang = "pl" if "pl" in accept_lang.lower() else "en"

    t = TRANSLATIONS[lang]

    form_data = {
        "hours": "74",
        "rate": "155.00",
        "ot_hours": "0",
        "ot_rate": "232.50",
        "sick_hours": "0",
        "sick_rate": "131.00",
        "bonus": "0",
        "fritvalg_pct": "9",
        "pension_pct": "2",
        "atp": "49.50",
        "other_ded": "0",
        "fradrag": "2200",
        "tax_pct": "38",
        "feriepenge": True,
        "pln_rate": "0.58"
    }
    result = None

    if request.method == "POST":
        hours = float(request.form.get("hours") or 0)
        rate = float(request.form.get("rate") or 0)
        ot_hours = float(request.form.get("ot_hours") or 0)
        ot_rate = float(request.form.get("ot_rate") or 0)
        sick_hours = float(request.form.get("sick_hours") or 0)
        sick_rate = float(request.form.get("sick_rate") or 0)
        bonus = float(request.form.get("bonus") or 0)
        fritvalg_pct = float(request.form.get("fritvalg_pct") or 0)
        pension_pct = float(request.form.get("pension_pct") or 0)
        atp = float(request.form.get("atp") or 0)
        other_ded = float(request.form.get("other_ded") or 0)
        fradrag = float(request.form.get("fradrag") or 0)
        tax_pct = float(request.form.get("tax_pct") or 0)
        feriepenge = "feriepenge" in request.form
        pln_rate = float(request.form.get("pln_rate") or 0.58)

        form_data = {
            "hours": hours,
            "rate": rate,
            "ot_hours": ot_hours,
            "ot_rate": ot_rate,
            "sick_hours": sick_hours,
            "sick_rate": sick_rate,
            "bonus": bonus,
            "fritvalg_pct": fritvalg_pct,
            "pension_pct": pension_pct,
            "atp": atp,
            "other_ded": other_ded,
            "fradrag": fradrag,
            "tax_pct": tax_pct,
            "feriepenge": feriepenge,
            "pln_rate": pln_rate
        }

        base_gross = hours * rate
        ot_gross = ot_hours * ot_rate
        sick_gross = sick_hours * sick_rate
        total_gross = base_gross + ot_gross + sick_gross + bonus

        # Składka emerytalna pracownika + stałe ATP odliczane przed AM-bidrag
        pension = total_gross * (pension_pct / 100.0)
        after_pension_and_atp = max(0.0, total_gross - pension - atp)

        # AM-bidrag 8%
        am_bidrag = after_pension_and_atp * 0.08
        after_am = after_pension_and_atp - am_bidrag

        # Podstawa opodatkowania A-skat
        taxable_income = max(0.0, after_am - fradrag)
        a_skat = taxable_income * (tax_pct / 100.0)

        # Feriepenge 12.5% (naliczane od godzin pracy, nadgodzin i dodatków - bez chorobowego)
        fp_eligible_gross = base_gross + ot_gross + bonus
        feriepenge_gross = fp_eligible_gross * 0.125 if feriepenge else 0.0
        feriepenge_tax = 0.0
        if feriepenge_gross > 0:
            fp_after_am = feriepenge_gross * 0.92
            feriepenge_tax = fp_after_am * (tax_pct / 100.0)

        # Fritvalgskonto (odkładane na osobne konto przez pracodawcę)
        fritvalg_gross = fp_eligible_gross * (fritvalg_pct / 100.0)

        netto = after_am - a_skat - feriepenge_tax - other_ded
        netto = max(0.0, netto)
        netto_pln = netto * pln_rate

        result = {
            "base_gross": base_gross,
            "ot_gross": ot_gross,
            "sick_gross": sick_gross,
            "bonus": bonus,
            "total_gross": total_gross,
            "pension": pension,
            "atp": atp,
            "am_bidrag": am_bidrag,
            "taxable_income": taxable_income,
            "a_skat": a_skat,
            "feriepenge_gross": feriepenge_gross,
            "feriepenge_tax": feriepenge_tax,
            "fritvalg_gross": fritvalg_gross,
            "other_ded": other_ded,
            "netto": netto,
            "netto_pln": netto_pln
        }

    return render_template_string(HTML_TEMPLATE, lang=lang, t=t, form=form_data, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
