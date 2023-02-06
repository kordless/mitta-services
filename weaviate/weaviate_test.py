import config
import weaviate

client = weaviate.Client(
    url="http://weaviate:f00bar@34.168.7.148:8088",
    additional_headers={
        "X-OpenAI-Api-Key": config.openai_token
    }
)


all_objects = client.data_object.get(class_name="History")
print(all_objects)
