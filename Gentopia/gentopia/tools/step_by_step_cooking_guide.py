from gentopia.tools.basetool import *

class StepByStepCookingGuideArgs(BaseModel):
    recipe: str = Field(..., description="The recipe for which instructions are needed")

class StepByStepCookingGuide(BaseTool):
    name = "step_by_step_cooking_guide"
    description = "Provides step-by-step instructions for cooking a recipe."

    args_schema: Optional[Type[BaseModel]] = StepByStepCookingGuideArgs

    def _run(self, recipe: str) -> str:
        instructions = {
            "Pasta with Tomato Sauce": (
                "1. Boil pasta in salted water.\n"
                "2. Heat oil in a pan, sauté garlic and onion.\n"
                "3. Add tomatoes and cook until soft.\n"
                "4. Mix cooked pasta with sauce, and serve."
            ),
            "Chicken Stir Fry": (
                "1. Heat oil in a wok.\n"
                "2. Add diced chicken and cook until browned.\n"
                "3. Add bell peppers and other vegetables.\n"
                "4. Stir fry with soy sauce and serve with rice."
            )
        }
        return instructions.get(recipe, f"No instructions available for {recipe}.")
    
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
