import subprocess
import json
import os
import asyncio
from typing import Dict, Any, Optional
from langchain.tools import tool

@tool
def fuel_transfer_tool(to_address: str, amount: str, asset_id: str = "default") -> str:
    """
    Transfer tokens on the Fuel blockchain.
    
    Args:
        to_address: The recipient's Fuel address (e.g., fuel1...).
        amount: The amount of tokens to transfer (as a string to preserve precision).
        asset_id: The asset ID of the token. Use 'default' for the base asset (ETH).
        
    Returns:
        A JSON string containing the transaction status, ID, and fee, or an error message.
    """
    bridge_path = os.path.join(os.path.dirname(__file__), "../bridge/transfer.ts")
    root_dir = os.path.join(os.path.dirname(__file__), "../../")
    
    # We use ts-node to execute our professional bridge script
    cmd = [
        "npx", "ts-node", bridge_path,
        to_address,
        asset_id,
        amount
    ]
    
    try:
        # Run the command and capture output
        result = subprocess.run(
            cmd,
            cwd=root_dir,
            capture_output=True,
            text=True,
            shell=True # Needed for npx on Windows
        )
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error executing transfer: {result.stderr.strip()}"
            
    except Exception as e:
        return f"System error calling Fuel bridge: {str(e)}"
