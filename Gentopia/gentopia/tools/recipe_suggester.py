from gentopia.tools.basetool import *
from typing import List

class RecipeSuggesterArgs(BaseModel):
    ingredients: List[str] = Field(..., description="List of available ingredients")

class RecipeSuggester(BaseTool):
    name = "recipe_suggester"
    description = "Suggests recipes based on available ingredients."

    args_schema: Optional[Type[BaseModel]] = RecipeSuggesterArgs

    def _run(self, ingredients: List[str]) -> str:
        # Example recipe suggestions (replace with real data)
        sample_recipes = {
            "tomato, onion, garlic": "Pasta with Tomato Sauce",
            "chicken, rice, bell pepper": "Chicken Stir Fry",
            "eggs, bread, cheese": "Cheese Omelette"
        }
        key = ", ".join(ingredients)
        return sample_recipes.get(key, "No recipe found for the provided ingredients.")
    
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
