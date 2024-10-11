from gentopia.tools.basetool import *

class DietaryRestrictionAdapterArgs(BaseModel):
    recipe: str = Field(..., description="The original recipe")
    restriction: str = Field(..., description="The dietary restriction to adapt to (e.g., vegan, gluten-free)")

class DietaryRestrictionAdapter(BaseTool):
    name = "dietary_restriction_adapter"
    description = "Adapts recipes to dietary restrictions."

    args_schema: Optional[Type[BaseModel]] = DietaryRestrictionAdapterArgs

    def _run(self, recipe: str, restriction: str) -> str:
        adapted_recipes = {
            "Pasta with Tomato Sauce - gluten-free": "Use gluten-free pasta instead of regular pasta.",
            "Chicken Stir Fry - vegan": "Replace chicken with tofu or seitan.",
        }
        key = f"{recipe} - {restriction}"
        return adapted_recipes.get(key, f"Cannot adapt {recipe} to {restriction}.")
    
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
