from flask import Flask, render_template_string, request

app = Flask(__name__)

TRANSLATIONS = {
    "pl": {
        "title": "Kalkulator Wypłaty Dania 2026 – Policz Netto (Lønseddel)",
        "header_title": "🇩🇰 Kalkulator Wypłaty Dania",
        "header_sub": "Sprawdź swoją wypłatę na rękę (netto) i zweryfikuj duński pasek (lønseddel)",
        "ad_top": "[Miejsce na reklamę Google AdSense – Baner Górny 728x90 / Responsywny]",
        "ad_bottom": "[Miejsce na reklamę Google AdSense – Baner Dolny / Artykułowy]",
        "quick_period": "Szybki wybór okresu / szablonu:",
        "btn_14d": "2 tygodnie (74h + ATP 49.50)",
        "btn_month": "Miesiąc (160.33h + ATP 99.00)",
        "btn_ot50": "Nadgodziny 50% (przelicznik)",
        "btn_sick_example": "Chorobowe 148h @ 137.43",
        "btn_clear_saved": "Wyczyść zapisane w przeglądarce",
        "saved_notice": "Przeglądarka automatycznie zapamiętuje Twoje ostatnie ustawienia na tym urządzeniu.",
        "sec_1": "1. Godziny i stawka podstawowa",
        "hours": "Liczba godzin zwykłych",
        "hours_hint": "Np. 160.33 (miesiąc) lub 74 (2 tyg.)",
        "rate": "Stawka godzinowa (DKK brutto)",
        "rate_hint": "Twoja podstawowa stawka z umowy",
        "sec_2": "2. Nadgodziny, chorobowe i dodatki",
        "ot_hours": "Nadgodziny (liczba godzin)",
        "ot_hours_hint": "Godziny ponad normę",
        "ot_pct": "Procent stawki nadgodzin (%)",
        "ot_pct_hint": "Np. 50% (gdy zakład płaci 50%), 100% lub 150%",
        "ot_rate": "Stawka za nadgodziny (DKK) – opcjonalnie ręcznie",
        "ot_rate_hint": "Zostaw 0, aby liczyło z % stawki podstawowej, lub wpisz kwotę",
        "sick_hours": "Godziny chorobowe (Sygeløn)",
        "sick_hours_hint": "Godziny na chorobowym / L4",
        "sick_rate": "Stawka za chorobowe (DKK)",
        "sick_rate_hint": "Np. 137.43 DKK, ~131 DKK lub 100% stawki",
        "hourly_bonus": "Dodatek za każdą godzinę (DKK/h)",
        "hourly_bonus_hint": "Np. dodatek zmianowy / chłodnia liczony × godziny",
        "bonus": "Inne dodatki ryczałtowe brutto (DKK)",
        "bonus_hint": "Nocki, regulacje, premie wpisane kwotowo",
        "fritvalg_pct": "Konto Fritvalgskonto (%)",
        "fritvalg_hint": "Dodatek odkładany przez firmę (zwykle 9% lub 0%)",
        "sec_3": "3. Podatki SKAT, emerytura, Feriepenge i przelewy",
        "fradrag": "Kwota wolna – Fradrag (DKK)",
        "fradrag_hint": "Kwota z paska dla danego okresu",
        "tax_pct": "Procent podatku – Trækprocent (%)",
        "tax_pct_hint": "Zwykle 36% – 42% (z karty podatkowej)",
        "pension_pct": "Składka emerytalna – Pension (%)",
        "pension_pct_hint": "Twój wkład własny (zwykle 0%, 2% lub 4%)",
        "atp": "Składka emerytalna ATP (DKK)",
        "atp_hint": "Stała kwota: 0, ~49.50–52.20 DKK/2 tyg. lub ~99 DKK/mies.",
        "netto_feriepenge": "Wypłacone Nettoferiepenge z paska (DKK)",
        "netto_feriepenge_hint": "Kwota netto zasiłku urlopowego doliczana do wypłaty",
        "tax_free_refund": "Zwrot nieopodatkowany / koszty (DKK)",
        "tax_free_refund_hint": "Np. zwrot za zaświadczenie lekarskie (np. 950 DKK)",
        "other_ded": "Inne potrącenia po podatku (DKK)",
        "other_ded_hint": "Np. związki, mieszkanie firmowe, inne potrącenia",
        "second_account": "Przelew na drugie konto / subkonto (DKK)",
        "second_account_hint": "Np. OVERFØRT TIL na DataLøn – odejmie od wypłaty na główne konto",
        "feriepenge": "Naliczaj <strong>Feriepenge (12,5%)</strong> od wynagrodzenia (standard dla pracowników godzinowych)",
        "round_taxes": "Zaokrąglaj podatki AM-bidrag i A-skat do pełnych koron (jak na pasku Zenegy / DataLøn)",
        "pln_rate": "Kurs wymiany DKK → PLN (do podglądu w złotówkach)",
        "btn_calc": "Oblicz moją wypłatę netto",
        "res_netto_label": "Szacowana wypłata netto łącznie:",
        "res_main_label": "Na konto główne (po przelewie na drugie konto):",
        "res_pln_info": "przy kursie",
        "res_breakdown": "Szczegółowe rozliczenie (jak na Lønseddel):",
        "row_base": "Wynagrodzenie podstawowe",
        "row_ot": "Nadgodziny",
        "row_sick": "Wynagrodzenie chorobowe (Sygeløn)",
        "row_hourly_bonus": "Dodatki godzinowe",
        "row_bonus": "Dodatki ryczałtowe (nocki / regulacje / premie)",
        "row_gross": "Suma wynagrodzenia brutto (Bruttoløn)",
        "row_fp_gross": "+ Odłożono na Feriepenge (12,5% na konto urlopowe)",
        "row_fv_gross": "+ Odłożono na Fritvalgskonto",
        "row_pension": "- Składka emerytalna pracownika (Pension)",
        "row_atp": "- Składka emerytalna ATP (ATP-bidrag)",
        "row_am": "- Podatek AM-bidrag (8%)",
        "row_taxable": "Podstawa opodatkowania (po odjęciu Fradrag)",
        "row_askat": "- Podatek dochodowy A-skat",
        "row_fp_tax": "- Podatek potrącony z góry za Feriepenge",
        "row_net_fp": "+ Wypłacone Nettoferiepenge (z paska)",
        "row_refund": "+ Zwrot nieopodatkowany (np. za lekarza)",
        "row_other_ded": "- Inne potrącenia po podatku",
        "row_second_acc": "- Przelew na drugie konto / subkonto",
        "row_main_payout": "Przelew na konto główne",
        "unit_h": "godz.",
        "aff_title": "💸 Wysyłasz wypłatę do Polski? Nie trać na kursie banku!",
        "aff_desc": "Duńskie banki pobierają nawet 3–4% ukrytej marży za przewalutowanie. Sprawdź przelew po kursie międzybankowym.",
        "aff_btn": "Sprawdź darmowy przelew DKK → PLN",
        "aff_alert": "Tutaj wstawisz swój link polecający do Wise lub Revolut!",
        "footer": "Kalkulator ma charakter poglądowy. Wyniki mogą się nieznacznie różnić w zależności od systemu płacowego (Zenegy / DataLøn) i zapisów na pasku (Lønseddel)."
    },
    "en": {
        "title": "Denmark Salary Calculator 2026 – Net Pay (Lønseddel)",
        "header_title": "🇩🇰 Denmark Salary Calculator",
        "header_sub": "Quickly calculate your net take-home pay and verify your Danish payslip (lønseddel)",
        "ad_top": "[Google AdSense Ad Slot – Top Banner 728x90 / Responsive]",
        "ad_bottom": "[Google AdSense Ad Slot – Bottom / In-Article Banner]",
        "quick_period": "Quick pay period / preset:",
        "btn_14d": "Bi-weekly (74h + ATP 49.50)",
        "btn_month": "Monthly (160.33h + ATP 99.00)",
        "btn_ot50": "Overtime 50% (rate %)",
        "btn_sick_example": "Sick pay 148h @ 137.43",
        "btn_clear_saved": "Clear saved browser values",
        "saved_notice": "Your browser automatically saves your last entered values on this device.",
        "sec_1": "1. Regular Hours & Base Rate",
        "hours": "Regular working hours",
        "hours_hint": "E.g. 160.33 (monthly) or 74 (bi-weekly)",
        "rate": "Hourly wage (DKK gross)",
        "rate_hint": "Your base hourly rate from contract",
        "sec_2": "2. Overtime, Sick Pay & Allowances",
        "ot_hours": "Overtime hours",
        "ot_hours_hint": "Extra hours worked",
        "ot_pct": "Overtime rate percentage (%)",
        "ot_pct_hint": "E.g. 50%, 100% or 150%",
        "ot_rate": "Overtime hourly rate (DKK) – optional manual override",
        "ot_rate_hint": "Leave 0 to compute from % of base rate, or enter custom rate",
        "sick_hours": "Sick leave hours (Sygeløn)",
        "sick_hours_hint": "Sick hours",
        "sick_rate": "Sick pay hourly rate (DKK)",
        "sick_rate_hint": "E.g. 137.43 DKK, ~131 DKK or 100% rate",
        "hourly_bonus": "Per-hour allowance (DKK/h)",
        "hourly_bonus_hint": "E.g. shift / cold storage allowance × hours",
        "bonus": "Other fixed gross allowances (DKK)",
        "bonus_hint": "Night shifts, adjustments, flat bonuses",
        "fritvalg_pct": "Fritvalgskonto savings (%)",
        "fritvalg_hint": "Employer-funded flexible account (usually 9% or 0%)",
        "sec_3": "3. SKAT Taxes, Pension, Feriepenge & Transfers",
        "fradrag": "Tax-free allowance – Fradrag (DKK)",
        "fradrag_hint": "Deduction amount shown on your payslip",
        "tax_pct": "Tax rate – Trækprocent (%)",
        "tax_pct_hint": "Usually 36% – 42% (from your tax card)",
        "pension_pct": "Employee pension contribution (%)",
        "pension_pct_hint": "Your own share (usually 0%, 2% or 4%)",
        "atp": "ATP Pension contribution (DKK)",
        "atp_hint": "Fixed fee: 0, ~49.50–52.20 DKK/2 weeks or ~99 DKK/month",
        "netto_feriepenge": "Paid Nettoferiepenge from payslip (DKK)",
        "netto_feriepenge_hint": "Net holiday pay amount added directly to take-home pay",
        "tax_free_refund": "Tax-free refund / expenses (DKK)",
        "tax_free_refund_hint": "E.g. medical certificate reimbursement (e.g. 950 DKK)",
        "other_ded": "Other post-tax deductions (DKK)",
        "other_ded_hint": "E.g. union fees, housing, other deductions",
        "second_account": "Transfer to second account / sub-account (DKK)",
        "second_account_hint": "E.g. OVERFØRT TIL on DataLøn – deducted from main account payout",
        "feriepenge": "Calculate <strong>Feriepenge (12.5%)</strong> holiday pay (standard for hourly workers)",
        "round_taxes": "Round AM-bidrag and A-skat to whole DKK (like Zenegy / DataLøn payslip)",
        "pln_rate": "Exchange rate DKK → EUR / PLN (optional preview)",
        "btn_calc": "Calculate My Net Salary",
        "res_netto_label": "Estimated Total Net Pay:",
        "res_main_label": "To main bank account (after second account transfer):",
        "res_pln_info": "at rate",
        "res_breakdown": "Detailed Payslip Breakdown (Lønseddel):",
        "row_base": "Base salary",
        "row_ot": "Overtime pay",
        "row_sick": "Sick pay (Sygeløn)",
        "row_hourly_bonus": "Per-hour allowances",
        "row_bonus": "Fixed allowances (night / adjustments / bonuses)",
        "row_gross": "Total Gross Salary (Bruttoløn)",
        "row_fp_gross": "+ Accrued Feriepenge (12.5% holiday account)",
        "row_fv_gross": "+ Accrued Fritvalgskonto",
        "row_pension": "- Employee Pension contribution",
        "row_atp": "- ATP Pension (ATP-bidrag)",
        "row_am": "- AM-bidrag tax (8%)",
        "row_taxable": "Taxable income (after Fradrag)",
        "row_askat": "- Income tax A-skat",
        "row_fp_tax": "- Pre-deducted tax on Feriepenge",
        "row_net_fp": "+ Paid Nettoferiepenge (from payslip)",
        "row_refund": "+ Tax-free refund (e.g. doctor fee)",
        "row_other_ded": "- Other post-tax deductions",
        "row_second_acc": "- Transfer to second account / sub-account",
        "row_main_payout": "Main bank account payout",
        "unit_h": "hrs",
        "aff_title": "💸 Sending money abroad from Denmark? Don't lose on bank fees!",
        "aff_desc": "Danish banks charge up to 3–4% in hidden exchange markups. Check real mid-market transfers.",
        "aff_btn": "Check Low-Cost International Transfer",
        "aff_alert": "Insert your Wise or Revolut affiliate link here!",
        "footer": "This calculator provides an estimate. Actual payout may vary slightly depending on payroll system (Zenegy / DataLøn) and payslip terms (Lønseddel)."
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="y5q2Zik_cDs3lX0-ACviLK6HZm5O2qmxbMMDu0TTcaU" />
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
            --blue: #1d4ed8;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }
        body { background: var(--bg); color: var(--text); line-height: 1.5; padding: 15px; }
        .container { max-width: 740px; margin: 0 auto; }

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
        .lang-btn.active { background: var(--primary); color: #ffffff; }

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
        .btn-reset { background: #fef2f2; border-color: #fecaca; color: #991b1b; }

        .saved-note {
            font-size: 0.78rem;
            color: var(--muted);
            margin-bottom: 14px;
            text-align: right;
        }

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
        input:focus { outline: none; border-color: var(--primary); background: #fff; }

        .checkbox-group {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 10px 0;
            background: #f9fafb;
            padding: 10px 12px;
            border-radius: 8px;
            border: 1px solid var(--border);
        }
        .checkbox-group input { width: 18px; height: 18px; accent-color: var(--primary); flex-shrink: 0; }
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
            margin-bottom: 12px;
        }
        .netto-highlight span { display: block; font-size: 0.9rem; color: #065f46; font-weight: 600; }
        .netto-highlight strong { font-size: 2rem; color: var(--green); }
        .netto-pln { font-size: 0.95rem; color: #047857; margin-top: 4px; }

        .main-account-box {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            padding: 12px 16px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 18px;
        }
        .main-account-box span { display: block; font-size: 0.85rem; color: #1e40af; font-weight: 600; }
        .main-account-box strong { font-size: 1.35rem; color: var(--blue); }

        table { width: 100%; border-collapse: collapse; font-size: 0.91rem; }
        td { padding: 9px 4px; border-bottom: 1px solid var(--border); }
        td:last-child { text-align: right; font-weight: 600; }
        tr.deduction td:last-child { color: #dc2626; }
        tr.addition td:last-child { color: var(--green); }
        tr.summary-row td { background: #f8fafc; font-weight: 700; }

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
                <button type="button" class="btn-preset" onclick="setOtPct(50)">{{ t.btn_ot50 }}</button>
                <button type="button" class="btn-preset" onclick="setSickExample()">{{ t.btn_sick_example }}</button>
                <button type="button" class="btn-preset btn-reset" onclick="clearSaved()">{{ t.btn_clear_saved }}</button>
            </div>
        </div>

        <div class="saved-note">{{ t.saved_notice }}</div>

        <form id="calc-form" method="POST" action="/?lang={{ lang }}">
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
                    <input type="number" step="0.01" id="rate" name="rate" value="{{ form.rate }}" required>
                </div>
            </div>

            <div class="section-title" style="margin-top: 14px;">{{ t.sec_2 }}</div>
            <div class="grid">
                <div class="form-group">
                    <label>{{ t.ot_hours }}
                        <span class="hint">{{ t.ot_hours_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="ot_hours" name="ot_hours" value="{{ form.ot_hours }}">
                </div>
                <div class="form-group">
                    <label>{{ t.ot_pct }}
                        <span class="hint">{{ t.ot_pct_hint }}</span>
                    </label>
                    <input type="number" step="0.1" id="ot_pct" name="ot_pct" value="{{ form.ot_pct }}">
                </div>
                <div class="form-group">
                    <label>{{ t.ot_rate }}
                        <span class="hint">{{ t.ot_rate_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="ot_rate" name="ot_rate" value="{{ form.ot_rate }}">
                </div>
                <div class="form-group">
                    <label>{{ t.sick_hours }}
                        <span class="hint">{{ t.sick_hours_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="sick_hours" name="sick_hours" value="{{ form.sick_hours }}">
                </div>
                <div class="form-group">
                    <label>{{ t.sick_rate }}
                        <span class="hint">{{ t.sick_rate_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="sick_rate" name="sick_rate" value="{{ form.sick_rate }}">
                </div>
                <div class="form-group">
                    <label>{{ t.hourly_bonus }}
                        <span class="hint">{{ t.hourly_bonus_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="hourly_bonus" name="hourly_bonus" value="{{ form.hourly_bonus }}">
                </div>
                <div class="form-group">
                    <label>{{ t.bonus }}
                        <span class="hint">{{ t.bonus_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="bonus" name="bonus" value="{{ form.bonus }}">
                </div>
                <div class="form-group">
                    <label>{{ t.fritvalg_pct }}
                        <span class="hint">{{ t.fritvalg_hint }}</span>
                    </label>
                    <input type="number" step="0.1" id="fritvalg_pct" name="fritvalg_pct" value="{{ form.fritvalg_pct }}">
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
                    <input type="number" step="0.1" id="tax_pct" name="tax_pct" value="{{ form.tax_pct }}" required>
                </div>
                <div class="form-group">
                    <label>{{ t.pension_pct }}
                        <span class="hint">{{ t.pension_pct_hint }}</span>
                    </label>
                    <input type="number" step="0.1" id="pension_pct" name="pension_pct" value="{{ form.pension_pct }}">
                </div>
                <div class="form-group">
                    <label>{{ t.atp }}
                        <span class="hint">{{ t.atp_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="atp" name="atp" value="{{ form.atp }}">
                </div>
                <div class="form-group">
                    <label>{{ t.netto_feriepenge }}
                        <span class="hint">{{ t.netto_feriepenge_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="netto_feriepenge" name="netto_feriepenge" value="{{ form.netto_feriepenge }}">
                </div>
                <div class="form-group">
                    <label>{{ t.tax_free_refund }}
                        <span class="hint">{{ t.tax_free_refund_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="tax_free_refund" name="tax_free_refund" value="{{ form.tax_free_refund }}">
                </div>
                <div class="form-group">
                    <label>{{ t.other_ded }}
                        <span class="hint">{{ t.other_ded_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="other_ded" name="other_ded" value="{{ form.other_ded }}">
                </div>
                <div class="form-group">
                    <label>{{ t.second_account }}
                        <span class="hint">{{ t.second_account_hint }}</span>
                    </label>
                    <input type="number" step="0.01" id="second_account" name="second_account" value="{{ form.second_account }}">
                </div>
            </div>

            <div class="checkbox-group">
                <input type="checkbox" id="feriepenge" name="feriepenge" {% if form.feriepenge %}checked{% endif %}>
                <label for="feriepenge">{{ t.feriepenge|safe }}</label>
            </div>

            <div class="checkbox-group">
                <input type="checkbox" id="round_taxes" name="round_taxes" {% if form.round_taxes %}checked{% endif %}>
                <label for="round_taxes">{{ t.round_taxes }}</label>
            </div>

            <div class="form-group">
                <label>{{ t.pln_rate }}</label>
                <input type="number" step="0.01" id="pln_rate" name="pln_rate" value="{{ form.pln_rate }}">
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

        {% if result.second_account > 0 %}
        <div class="main-account-box">
            <span>{{ t.res_main_label }}</span>
            <strong>{{ "%.2f"|format(result.main_payout) }} DKK</strong>
            <div class="netto-pln" style="color: #1d4ed8;">≈ {{ "%.2f"|format(result.main_payout_pln) }} PLN</div>
        </div>
        {% endif %}

        <div class="section-title">{{ t.res_breakdown }}</div>
        <table>
            <tr>
                <td>{{ t.row_base }} ({{ form.hours }} {{ t.unit_h }})</td>
                <td>{{ "%.2f"|format(result.base_gross) }} DKK</td>
            </tr>
            {% if result.ot_gross > 0 %}
            <tr>
                <td>{{ t.row_ot }} ({{ form.ot_hours }} {{ t.unit_h }}, {{ "%.2f"|format(result.effective_ot_rate) }} DKK/h)</td>
                <td>{{ "%.2f"|format(result.ot_gross) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.sick_gross > 0 %}
            <tr>
                <td>{{ t.row_sick }} ({{ form.sick_hours }} {{ t.unit_h }})</td>
                <td>{{ "%.2f"|format(result.sick_gross) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.hourly_bonus_total > 0 %}
            <tr>
                <td>{{ t.row_hourly_bonus }} ({{ form.hourly_bonus }} DKK/h)</td>
                <td>{{ "%.2f"|format(result.hourly_bonus_total) }} DKK</td>
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
            {% if result.netto_feriepenge > 0 %}
            <tr class="addition">
                <td>{{ t.row_net_fp }}</td>
                <td>+{{ "%.2f"|format(result.netto_feriepenge) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.tax_free_refund > 0 %}
            <tr class="addition">
                <td>{{ t.row_refund }}</td>
                <td>+{{ "%.2f"|format(result.tax_free_refund) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.other_ded > 0 %}
            <tr class="deduction">
                <td>{{ t.row_other_ded }}</td>
                <td>-{{ "%.2f"|format(result.other_ded) }} DKK</td>
            </tr>
            {% endif %}
            {% if result.second_account > 0 %}
            <tr class="deduction">
                <td>{{ t.row_second_acc }}</td>
                <td>-{{ "%.2f"|format(result.second_account) }} DKK</td>
            </tr>
            <tr class="summary-row">
                <td>{{ t.row_main_payout }}</td>
                <td>{{ "%.2f"|format(result.main_payout) }} DKK</td>
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
const STORAGE_KEY = "paycalcdk_form_v2";
const FIELD_IDS = [
    "hours", "rate", "ot_hours", "ot_pct", "ot_rate",
    "sick_hours", "sick_rate", "hourly_bonus", "bonus",
    "fritvalg_pct", "fradrag", "tax_pct", "pension_pct",
    "atp", "netto_feriepenge", "tax_free_refund",
    "other_ded", "second_account", "pln_rate"
];
const CHECKBOX_IDS = ["feriepenge", "round_taxes"];

function saveFormState() {
    const data = {};
    FIELD_IDS.forEach(id => {
        const el = document.getElementById(id);
        if (el) data[id] = el.value;
    });
    CHECKBOX_IDS.forEach(id => {
        const el = document.getElementById(id);
        if (el) data[id] = el.checked;
    });
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(data)); } catch (e) {}
}

function loadFormState() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) return;
        const data = JSON.parse(raw);
        FIELD_IDS.forEach(id => {
            const el = document.getElementById(id);
            if (el && data[id] !== undefined) el.value = data[id];
        });
        CHECKBOX_IDS.forEach(id => {
            const el = document.getElementById(id);
            if (el && typeof data[id] === "boolean") el.checked = data[id];
        });
    } catch (e) {}
}

function clearSaved() {
    try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
    window.location.href = "/?lang={{ lang }}";
}

function resetExtraFields() {
    document.getElementById("ot_hours").value = "0";
    document.getElementById("ot_rate").value = "0";
    document.getElementById("sick_hours").value = "0";
    document.getElementById("hourly_bonus").value = "0";
    document.getElementById("bonus").value = "0";
    document.getElementById("fritvalg_pct").value = "0";
    document.getElementById("netto_feriepenge").value = "0";
    document.getElementById("tax_free_refund").value = "0";
    document.getElementById("other_ded").value = "0";
    document.getElementById("second_account").value = "0";
}

function setPreset(hours, atp, fradrag) {
    resetExtraFields();
    document.getElementById("hours").value = hours;
    document.getElementById("atp").value = atp.toFixed(2);
    document.getElementById("fradrag").value = fradrag;
    document.getElementById("feriepenge").checked = true;
    document.getElementById("round_taxes").checked = true;
    saveFormState();
}

function setOtPct(pct) {
    document.getElementById("ot_pct").value = pct;
    document.getElementById("ot_rate").value = "0";
    saveFormState();
}

function setSickExample() {
    resetExtraFields();
    document.getElementById("hours").value = "0";
    document.getElementById("rate").value = "0";
    document.getElementById("sick_hours").value = "148";
    document.getElementById("sick_rate").value = "137.43";
    document.getElementById("pension_pct").value = "4";
    document.getElementById("atp").value = "0";
    document.getElementById("fradrag").value = "6302";
    document.getElementById("tax_pct").value = "38";
    document.getElementById("netto_feriepenge").value = "1450.46";
    document.getElementById("feriepenge").checked = false;
    document.getElementById("round_taxes").checked = true;
    saveFormState();
}

document.addEventListener("DOMContentLoaded", () => {
    const hasPostResult = {{ "true" if result else "false" }};
    if (!hasPostResult) {
        loadFormState();
    } else {
        saveFormState();
    }
    FIELD_IDS.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.addEventListener("change", saveFormState);
    });
    CHECKBOX_IDS.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.addEventListener("change", saveFormState);
    });
});
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
        "ot_pct": "150",
        "ot_rate": "0",
        "sick_hours": "0",
        "sick_rate": "131.00",
        "hourly_bonus": "0",
        "bonus": "0",
        "fritvalg_pct": "0",
        "pension_pct": "2",
        "atp": "49.50",
        "netto_feriepenge": "0",
        "tax_free_refund": "0",
        "other_ded": "0",
        "second_account": "0",
        "fradrag": "2200",
        "tax_pct": "38",
        "feriepenge": True,
        "round_taxes": True,
        "pln_rate": "0.58"
    }
    result = None

    if request.method == "POST":
        hours = float(request.form.get("hours") or 0)
        rate = float(request.form.get("rate") or 0)
        ot_hours = float(request.form.get("ot_hours") or 0)
        ot_pct = float(request.form.get("ot_pct") or 150)
        ot_rate_input = float(request.form.get("ot_rate") or 0)
        sick_hours = float(request.form.get("sick_hours") or 0)
        sick_rate = float(request.form.get("sick_rate") or 0)
        hourly_bonus = float(request.form.get("hourly_bonus") or 0)
        bonus = float(request.form.get("bonus") or 0)
        fritvalg_pct = float(request.form.get("fritvalg_pct") or 0)
        pension_pct = float(request.form.get("pension_pct") or 0)
        atp = float(request.form.get("atp") or 0)
        netto_feriepenge = float(request.form.get("netto_feriepenge") or 0)
        tax_free_refund = float(request.form.get("tax_free_refund") or 0)
        other_ded = float(request.form.get("other_ded") or 0)
        second_account = float(request.form.get("second_account") or 0)
        fradrag = float(request.form.get("fradrag") or 0)
        tax_pct = float(request.form.get("tax_pct") or 0)
        feriepenge = "feriepenge" in request.form
        round_taxes = "round_taxes" in request.form
        pln_rate = float(request.form.get("pln_rate") or 0.58)

        form_data = {
            "hours": hours,
            "rate": rate,
            "ot_hours": ot_hours,
            "ot_pct": ot_pct,
            "ot_rate": ot_rate_input,
            "sick_hours": sick_hours,
            "sick_rate": sick_rate,
            "hourly_bonus": hourly_bonus,
            "bonus": bonus,
            "fritvalg_pct": fritvalg_pct,
            "pension_pct": pension_pct,
            "atp": atp,
            "netto_feriepenge": netto_feriepenge,
            "tax_free_refund": tax_free_refund,
            "other_ded": other_ded,
            "second_account": second_account,
            "fradrag": fradrag,
            "tax_pct": tax_pct,
            "feriepenge": feriepenge,
            "round_taxes": round_taxes,
            "pln_rate": pln_rate
        }

        effective_ot_rate = ot_rate_input if ot_rate_input > 0 else rate * (ot_pct / 100.0)
        base_gross = hours * rate
        ot_gross = ot_hours * effective_ot_rate
        sick_gross = sick_hours * sick_rate
        active_hours = hours + ot_hours + sick_hours
        hourly_bonus_total = round(active_hours * hourly_bonus, 2)
        total_gross = base_gross + ot_gross + sick_gross + hourly_bonus_total + bonus

        pension = round(total_gross * (pension_pct / 100.0), 2)
        after_pension_and_atp = max(0.0, total_gross - pension - atp)

        raw_am = after_pension_and_atp * 0.08
        am_bidrag = float(round(raw_am)) if round_taxes else round(raw_am, 2)
        after_am = after_pension_and_atp - am_bidrag

        taxable_income = max(0.0, after_am - fradrag)
        raw_askat = taxable_income * (tax_pct / 100.0)
        a_skat = float(round(raw_askat)) if round_taxes else round(raw_askat, 2)

        fp_eligible_gross = base_gross + ot_gross + hourly_bonus_total + bonus
        feriepenge_gross = round(fp_eligible_gross * 0.125, 2) if feriepenge else 0.0
        feriepenge_tax = 0.0
        if feriepenge_gross > 0:
            fp_after_am = feriepenge_gross * 0.92
            raw_fp_tax = fp_after_am * (tax_pct / 100.0)
            feriepenge_tax = float(round(raw_fp_tax)) if round_taxes else round(raw_fp_tax, 2)

        fritvalg_gross = round(fp_eligible_gross * (fritvalg_pct / 100.0), 2)

        netto = after_am - a_skat - feriepenge_tax + netto_feriepenge + tax_free_refund - other_ded
        netto = max(0.0, round(netto, 2))
        netto_pln = round(netto * pln_rate, 2)

        main_payout = max(0.0, round(netto - second_account, 2))
        main_payout_pln = round(main_payout * pln_rate, 2)

        result = {
            "base_gross": base_gross,
            "ot_gross": ot_gross,
            "effective_ot_rate": effective_ot_rate,
            "sick_gross": sick_gross,
            "hourly_bonus_total": hourly_bonus_total,
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
            "netto_feriepenge": netto_feriepenge,
            "tax_free_refund": tax_free_refund,
            "other_ded": other_ded,
            "second_account": second_account,
            "netto": netto,
            "netto_pln": netto_pln,
            "main_payout": main_payout,
            "main_payout_pln": main_payout_pln
        }

    return render_template_string(HTML_TEMPLATE, lang=lang, t=t, form=form_data, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
