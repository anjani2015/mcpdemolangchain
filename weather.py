#from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool
async def get_weather_details(location:str)->str:
    """
    Get the weather details based on the location.
    """
    return "Its rainy season all over the INDIA"

if __name__=="__main__":
    mcp.run(transport="streamable-http")