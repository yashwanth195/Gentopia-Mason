from typing import AnyStr
from gentopia.tools.basetool import *
from PyPDF2 import PdfReader
import io
import requests


class PdfreaderArgs(BaseModel):
    url: str = Field(..., description="read a url")


class Pdfreader(BaseTool):
    """Tool that adds the capability to query the Google search API."""

    name = "pdf_reader"
    description = ("Read the PDF."
                   "Input should be a pdf url.")

    args_schema: Optional[Type[BaseModel]] = PdfreaderArgs

    def _run(self, url: AnyStr) -> str:
        response=requests.get(url)
        if response.status_code!=200:
            raise Exception("unable to read the url")
        pdfreader=PdfReader(io.BytesIO(response.content))
        content=""
        for page in pdfreader.pages:
            content += page.extract_text()

        return content
    
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = Pdfreader()._run("Attention for transformer")
    print(ans)
