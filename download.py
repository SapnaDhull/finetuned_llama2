from huggingface_hub import snapshot_download
model_id="preetrathee/Llama-2-7b-chat-finetune"
snapshot_download(repo_id=model_id, local_dir="sapna-llama2",
                  local_dir_use_symlinks=False, revision="main")