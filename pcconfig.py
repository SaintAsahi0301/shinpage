import pynecone as pc

config = pc.Config(
    app_name="shinpage",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=3001
)
