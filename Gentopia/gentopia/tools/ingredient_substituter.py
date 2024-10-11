from gentopia.tools.basetool import *

class IngredientSubstituterArgs(BaseModel):
    ingredient: str = Field(..., description="The ingredient to be substituted")

class IngredientSubstituter(BaseTool):
    name = "ingredient_substituter"
    description = "Provides alternative ingredients for dietary restrictions or missing items."

    args_schema: Optional[Type[BaseModel]] = IngredientSubstituterArgs

    def _run(self, ingredient: str) -> str:
        substitutions = {
            "milk": "almond milk, soy milk, coconut milk",
            "egg": "flaxseed meal, applesauce, chia seeds",
            "flour": "gluten-free flour, almond flour, coconut flour"
        }
        return substitutions.get(ingredient, f"No substitution found for {ingredient}")
    
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
