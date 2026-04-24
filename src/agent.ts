import { ChatPromptTemplate } from '@langchain/core/prompts';
import { ChatOpenAI } from '@langchain/openai';
import { createToolCallingAgent, AgentExecutor } from 'langchain/agents';
import { createTools } from './tools.js';
import { modelMapping } from './utils/models.js';
import { ChatAnthropic } from '@langchain/anthropic';
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
import { SystemMessage } from '@langchain/core/messages';

const systemMessage = new SystemMessage(
  `You are an AI agent on Fuel network capable of executing all kinds of transactions and interacting with the Fuel blockchain.
You are able to execute transactions on behalf of the user.

I...AllVerifiedFuelAssets();
const asset = allAssets.find((asset) => asset.symbol === params.symbol);
const assetId = asset?.assetId;

const weiAmount = bn.parseUnits(params.amount, asset?.decimals);

const tx = await marketContract.functions
  .supply_collateral()
  .callParams({
    forward: {
      assetId: assetId,
      amount: weiAmount,
    } as any,
  })
  .call();

const { transactionId } = await tx.waitForResult();

return JSON.stringify({
  status: 'success',
  id: transactionId,
  link: getTxExplorerUrl(transactionId),
});
} catch (error) {
return JSON.stringify({
  status: 'failure',
  error: error instanceof Error ? error.message : 'Unknown error',
});
}
};

const tools = createTools();
const llm = new ChatOpenAI({
  temperature: 0,
  apiKey: process.env.OPENAI_API_KEY,
});

const agent = createToolCallingAgent({
  tools,
  llm,
  agent: 'zero-shot-react-description',
});

export const agentExecutor = new AgentExecutor(agent);

export async function runAgent(input: string) {
  const agentResponse = await agentExecutor.run(input);
  return agentResponse;
}