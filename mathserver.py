from fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def multiplication(a:int, b:int)-> int:
    """summary
    Multiplation of two numbers
    """
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")
