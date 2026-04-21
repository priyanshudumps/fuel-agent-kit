import { Wallet, Provider, bn, BaseAssetId } from 'fuels';
import * as dotenv from 'dotenv';
import * as path from 'path';

// Load environment variables from the root .env
dotenv.config({ path: path.resolve(__dirname, '../../.env') });

async function main() {
    const args = process.argv.slice(2);
    if (args.length < 3) {
        console.error('Usage: ts-node transfer.ts <to_address> <token_asset_id> <amount>');
        process.exit(1);
    }

    const [toAddress, assetId, amount] = args;
    const privateKey = process.env.FUEL_WALLET_PRIVATE_KEY;
    const providerUrl = process.env.FUEL_NETWORK_URL || 'https://testnet.fuel.network/v1/graphql';

    if (!privateKey) {
        console.error('Error: FUEL_WALLET_PRIVATE_KEY not found in .env');
        process.exit(1);
    }

    try {
        const provider = await Provider.create(providerUrl);
        const wallet = Wallet.fromPrivateKey(privateKey, provider);
        
        // Use provided assetId or default to base asset
        const targetAssetId = assetId === 'default' ? await provider.getBaseAssetId() : assetId;

        console.log(`Initiating transfer of ${amount} to ${toAddress}...`);
        
        // Perform the transfer
        const response = await wallet.transfer(
            toAddress,
            bn.parseUnits(amount), // Handling units correctly
            targetAssetId
        );

        const result = await response.waitForResult();
        console.log(JSON.stringify({
            status: 'success',
            transactionId: result.id,
            fee: result.fee.toString(),
            block: result.blockId
        }));
    } catch (error: any) {
        console.error(JSON.stringify({
            status: 'error',
            message: error.message
        }));
        process.exit(1);
    }
}

main();
