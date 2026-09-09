def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    normalized_ingredients = ingredients.lower()
    allowed_ingredients = light_spell_allowed_ingredients()
    is_valid = any(
        ingredient in normalized_ingredients
        for ingredient in allowed_ingredients
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
