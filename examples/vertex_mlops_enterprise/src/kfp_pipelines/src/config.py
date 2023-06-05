from train import REGION, PROJECT_NR, PROJECT_ID

MY_STAGING_BUCKET = PROJECT_ID
PIPELINE_NAME = 'xgb-creditcards'
PIPELINE_ROOT = f'gs://{MY_STAGING_BUCKET}/pipeline_root/{PIPELINE_NAME}'

BQ_INPUT_DATA=f"{PROJECT_ID}.vertex_eu.creditcards"
PARENT_MODEL='projects/{PROJECT_NR}/locations/{REGION}}/models/7109310243804282880'

MODEL_CARD_CONFIG='../model_card_config.json'