# Databricks notebook source
# MAGIC %md
# MAGIC # Forks: the alternatives
# MAGIC
# MAGIC The notebook `fraud_triage_agent` is the **chosen path**, end to end. This file holds the **strongest alternative** at each decision point (fork).
# MAGIC
# MAGIC **The contract:** every fork takes the same input (the state dict) and returns the same output as the notebook's version. Only the inside is different.
# MAGIC
# MAGIC **How to run:** from the notebook, `%run ./forks`, after `call_llm`, `small_llm` and `POLICIES` exist.
# MAGIC
# MAGIC | Fork | Notebook (chosen) | This file (alternative) | I'd switch when |
# MAGIC |---|---|---|---|
# MAGIC | 01 Planner output shape | Pydantic class `Plan` | hand-written JSON Schema dict `plan_shape` | [fill] |
# MAGIC | 02 How the node calls the model | structured output | raw call + `json.loads` | [fill] |

# COMMAND ----------

# MAGIC %md
# MAGIC ## Fork 01: Planner output shape, as a hand-written JSON Schema
# MAGIC Same 2 fields as the Pydantic `Plan` class in the notebook. This is what Pydantic generates underneath.

# COMMAND ----------

# ---- FORK 01: the Planner's answer format as a JSON Schema dict ----

# >>> PASTE YOUR plan_shape HERE (cut it from the notebook) <<<



# planner_manual_schema(state):
#   same steps as planner() in the notebook, but calls call_llm(..., shape=plan_shape)
#   the answer comes back as a dict, so read answer['story_vs_data'], answer['checks']
#   returns the same 3 fields: story_vs_data, checks, difficulty
# >>> YOU WRITE THIS after the notebook planner works <<<

# COMMAND ----------

# MAGIC %md
# MAGIC ## Fork 02: How the node calls the model, raw call + json.loads
# MAGIC No structured output. The prompt asks for JSON, and we parse the text ourselves.

# COMMAND ----------

# planner_raw_parse(state):
#   same inputs; the prompt ends with "Reply only with JSON: {...}"
#   call_llm(small_llm, prompt, "planner_raw") with NO shape -> a string
#   json.loads(that string) -> a dict (this is where it can break)
#   returns the same 3 fields: story_vs_data, checks, difficulty
# >>> YOU WRITE THIS after fork 01 <<<
