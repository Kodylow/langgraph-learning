# First, source your local .env file
set -a
source .env
set +a

# Then create and populate the module .env files
for i in {1..4}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" >module-$i/studio/.env

  # Add LANGCHAIN keys to all modules
  echo "LANGCHAIN_API_KEY=\"$LANGCHAIN_API_KEY\"" >>module-$i/studio/.env
  echo "LANGCHAIN_TRACING_V2=\"$LANGCHAIN_TRACING_V2\"" >>module-$i/studio/.env
done

# Add Tavily key to module-4 only
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >>module-4/studio/.env
