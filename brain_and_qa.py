"""
Holy Snack AI Content & FSANZ Compliance Engine (brain_and_qa.py)
Author: Nithin Choudhary — Final October Deliverable (100% NIP-Verified Edition)
"""
import re

VERIFIED_NIP_DB = {
    "Himalayan Salt": {
        "barcode": "0783970960504",
        "price_aud": 12.00,
        "pack_weight_g": 60,
        "serving_size_g": 30,
        "energy_kj_30g": 664,
        "energy_kcal_30g": 159,
        "protein_g_30g": 2.3,
        "fat_g_30g": 9.5,
        "sat_fat_g_30g": 1.6,
        "trans_fat_g_30g": 0.0,
        "carbs_g_30g": 15.8,
        "sugars_g_30g": 0.0,
        "fibre_g_30g": 0.7,
        "sodium_mg_30g": 192,
        "cholesterol_mg_30g": 0,
        "ingredients": "Popped water lily seed (70%), Olive oil, Himalayan salt (5.5%), Rosemary extract.",
        "direct_allergens": None,
        "may_contain": "Almond, Cashew, Egg, Hazelnut, Lupin, Macadamia, Milk, Peanut, Pinenut, Sesame, Soy, Sulphites, Walnut"
    },
    "Peri Peri": {
        "barcode": "0783970960498",
        "price_aud": 12.00,
        "pack_weight_g": 60,
        "serving_size_g": 30,
        "energy_kj_30g": 618,
        "energy_kcal_30g": 148,
        "protein_g_30g": 2.3,
        "fat_g_30g": 7.4,
        "sat_fat_g_30g": 1.2,
        "trans_fat_g_30g": 0.0,
        "carbs_g_30g": 17.8,
        "sugars_g_30g": 0.5,
        "fibre_g_30g": 0.5,
        "sodium_mg_30g": 192,
        "cholesterol_mg_30g": 0,
        "ingredients": "Popped water lily seed (69%), Olive oil, Peri Peri blend (6.5%), Rosemary extract.",
        "direct_allergens": None,
        "may_contain": "Almond, Cashew, Egg, Hazelnut, Lupin, Macadamia, Milk, Peanut, Pinenut, Sesame, Soy, Sulphites, Walnut"
    },
    "Thai Sweet Chilli": {
        "barcode": "0783970960511",
        "price_aud": 12.00,
        "pack_weight_g": 60,
        "serving_size_g": 30,
        "energy_kj_30g": 618,
        "energy_kcal_30g": 148,
        "protein_g_30g": 2.3,
        "fat_g_30g": 7.3,
        "sat_fat_g_30g": 1.2,
        "trans_fat_g_30g": 0.0,
        "carbs_g_30g": 18.0,
        "sugars_g_30g": 0.6,
        "fibre_g_30g": 0.4,
        "sodium_mg_30g": 102,
        "cholesterol_mg_30g": 0,
        "ingredients": "Popped water lily seed (68%), Olive oil, Thai Sweet Chilli blend (8%) [Contains Hydrolysed vegetable protein (Peanut)], Rosemary extract.",
        "direct_allergens": "CONTAINS: PEANUT",
        "may_contain": "Almond, Cashew, Egg, Hazelnut, Lupin, Macadamia, Milk, Peanut, Pinenut, Sesame, Soy, Sulphites, Walnut"
    }
}

FORBIDDEN_CLAIMS_REGEX = [
    (r"\bnut[- ]?free\b", "BLOCKED (Allergen Risk): Thai Sweet Chilli contains Peanut, and all SKUs carry a 'May Contain Tree Nuts/Peanuts' statement."),
    (r"\bpeanut[- ]?free\b", "BLOCKED (Allergen Risk): Thai Sweet Chilli contains Hydrolysed vegetable protein (Peanut)."),
    (r"\bhigh[- ]?protein\b", "BLOCKED (FSANZ Schedule 4): Pack has 2.3g protein/30g serve (<10g threshold). Use '2.3g plant-based protein/serve'."),
    (r"\bhigh[- ]?fib(re|er)\b", "BLOCKED (FSANZ Schedule 4): Pack has 0.4g-0.7g fibre/serve (<4g threshold)."),
    (r"\blow[- ]?gi\b", "BLOCKED (FSANZ s 1.2.7-12(6)): Requires numerical GI value printed on NIP."),
    (r"\bketo\b", "BLOCKED (Macro Conflict): Makhana is 52.5g-60.1g carbs per 100g."),
    (r"\blow[- ]?calorie\b", "BLOCKED (FSANZ Schedule 4): Requires <=170 kJ/100g. Use '148-159 calories per 30g serve' instead."),
    (r"\bafterncon\b", "BLOCKED (Typo Catch): Correct 'Afterncon' to 'Afternoon'.")
]

def run_qa_firewall(draft_text: str, sku: str = "Peri Peri") -> dict:
    issues = []
    for pattern, reason in FORBIDDEN_CLAIMS_REGEX:
        if re.search(pattern, draft_text, flags=re.IGNORECASE):
            issues.append(reason)
    if sku in ["Peri Peri", "Thai Sweet Chilli"] and re.search(r"no artificial|msg[- ]?free|4 ingredients", draft_text, re.IGNORECASE):
        issues.append("BLOCKED (Ingredient Scope): '4 ingredients / no artificial flavours or enhancers' applies ONLY to Himalayan Salt.")
    return {
        "passed": len(issues) == 0,
        "sku_checked": sku,
        "issues_found": issues,
        "verified_nip_reference": VERIFIED_NIP_DB.get(sku, {})
    }

if __name__ == "__main__":
    sample = "Grab our Peri Peri Fox Nuts — gently roasted in olive oil in Melbourne at 148 calories per 30g serve!"
    print(run_qa_firewall(sample, "Peri Peri"))
