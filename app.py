
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

#######################################################
## 今回検索対象とするカタログとスキーマを選択します。   #######
#######################################################

catalog = "samples"
schema = "nyctaxi" 
tables  = ["trips"] 
host = os.environ.get("DATABRICKS_HOST") 
warehouse_id = os.environ.get("DATABRICKS_WAREHOUSE") 
api_token = os.environ.get("DATABRICKS_TOKEN")

# LLM
llm = OpenAI(temperature=0, verbose=True)

## Langchain SQLDatabaseChain
db = SQLDatabase.from_databricks(catalog=catalog, 
                                 schema=schema, 
                                 include_tables=tables, 
                                 host = host, 
                                 warehouse_id=warehouse_id, 
                                 api_token=api_token)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

#######################################################
# ここから Slack 設定
# トークンとソケットモードハンドラーを使ってアプリを初期化します
#######################################################

app = App(token=os.environ.get("SLACK_BOT_TOKEN")) 

# mentionされた場合メッセージを読み取ります
@app.event("app_mention")
def respond_to_mention(body, say):
    channel_id = body["event"]["channel"]
    user_id = body["event"]["user"]
    question = body["event"]["text"]

    response = db_chain.run(question)

    # Craft your response message
    message = f"Answer: {response}"

    # Send the response message
    say(message, channel=channel_id)

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()