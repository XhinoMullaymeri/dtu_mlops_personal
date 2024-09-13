from dotenv import load_dotenv
load_dotenv()
import os


print(f"'XHINO_TEMP_VAR' env var value is : '{os.environ['XHINO_TEMP_VAR']}'")
print(f"'XHINO_TEMP_VAR_DOTENV' .env var value is : '{os.environ['XHINO_TEMP_VAR_DOTENV']}'")
