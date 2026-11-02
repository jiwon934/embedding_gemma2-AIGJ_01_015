---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:303
- loss:MatryoshkaLoss
- loss:MultipleNegativesRankingLoss
base_model: google/embeddinggemma-2
widget:
- source_sentence: 장비 대여 절차
  sentences:
  - 장비를 빌려 갈 때는 대여 대장에 이름과 반납 예정일을 적는다.
  - 음식 냄새가 남지 않도록 강의실 안에서는 뚜껑 있는 음료만 허용한다.
  - 장비를 빌려 갈 때는 대여 대장에 이름과 반납 예정일을 적는다.
- source_sentence: 필터 세척 주기
  sentences:
  - 냉방기 설정 온도를 1도 높이면 전력 사용량이 약 7% 줄어든다.
  - 에어컨 필터는 2주마다 먼지를 털어내고 한 달마다 물로 세척한다.
  - 에어컨 필터는 2주마다 먼지를 털어내고 한 달마다 물로 세척한다.
- source_sentence: 개인 정보 조회 권한
  sentences:
  - 냉난방기 실외기 주변에 물건을 두면 효율이 떨어지고 고장 원인이 된다.
  - 에이전트에게 개인 정보나 출석 기록 조회는 허용하지 않는다.
  - 최종 발표는 팀당 15분이며 시연 영상과 슬라이드를 함께 준비한다.
- source_sentence: 냉방비 줄이는 방법
  sentences:
  - 냉방기 설정 온도를 1도 높이면 전력 사용량이 약 7% 줄어든다.
  - 음식 냄새가 남지 않도록 강의실 안에서는 뚜껑 있는 음료만 허용한다.
  - 장비를 빌려 갈 때는 대여 대장에 이름과 반납 예정일을 적는다.
- source_sentence: 출결 처리 방법
  sentences:
  - 최종 발표는 팀당 15분이며 시연 영상과 슬라이드를 함께 준비한다.
  - 결석이나 지각은 오전 9시 10분까지 출결 시스템에 사유를 입력한다.
  - 강의 자료와 실습 코드는 매주 월요일 오전에 과정 저장소에 올라온다.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: SentenceTransformer based on google/embeddinggemma-2
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: classroom
      type: classroom
    metrics:
    - type: cosine_accuracy@1
      value: 0.85
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.9666666666666667
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9833333333333333
      name: Cosine Accuracy@5
    - type: cosine_precision@1
      value: 0.85
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.32222222222222213
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.19666666666666663
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09999999999999996
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.85
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.9666666666666667
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.9833333333333333
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 1.0
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.9341598068805912
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.9121031746031747
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.9121031746031746
      name: Cosine Map@100
---

# SentenceTransformer based on google/embeddinggemma-2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [google/embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2) on the json dataset. It maps inputs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [google/embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2) <!-- at revision 914f7f89142e33e77833254d9c9b90c3cef7303b -->
- **Maximum Sequence Length:** 1000000000000000019884624838656 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modalities:** Text, Image, Audio, Video, Message
- **Training Dataset:**
    - json
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'image': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'audio': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'video': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'message': {'method': 'forward', 'method_output_name': 'last_hidden_state', 'format': 'structured'}}, 'module_output_name': 'token_embeddings', 'architecture': 'EmbeddingGemma2Model'})
  (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({'module_input_name': 'sentence_embedding', 'module_output_name': 'sentence_embedding'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
queries = [
    '오후만 되면 다들 졸아요',
]
documents = [
    'CO2 농도가 1000ppm을 넘으면 졸음과 두통이 늘어나므로 즉시 환기한다.',
    'CO2가 1500ppm 이상으로 20분 넘게 유지되면 경고 단계로 올리고 수업 중이라도 창문을 연다.',
    '외기 CO2는 보통 420ppm 안팎이라 환기 후 실내 값도 450ppm 근처까지 떨어진다.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 768] [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[0.5171, 0.4122, 0.3276]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Information Retrieval

* Dataset: `classroom`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "query_prompt_name": "SearchQuery",
      "corpus_prompt_name": "Document"
  }
  ```

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.85       |
| cosine_accuracy@3   | 0.9667     |
| cosine_accuracy@5   | 0.9833     |
| cosine_precision@1  | 0.85       |
| cosine_precision@3  | 0.3222     |
| cosine_precision@5  | 0.1967     |
| cosine_precision@10 | 0.1        |
| cosine_recall@1     | 0.85       |
| cosine_recall@3     | 0.9667     |
| cosine_recall@5     | 0.9833     |
| cosine_recall@10    | 1.0        |
| **cosine_ndcg@10**  | **0.9342** |
| cosine_mrr@10       | 0.9121     |
| cosine_map@100      | 0.9121     |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### json

* Dataset: json
* Size: 303 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 100 samples:
  |          | anchor                                                                            | positive                                                                           |
  |:---------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type     | string                                                                            | string                                                                             |
  | modality | text                                                                              | text                                                                               |
  | details  | <ul><li>min: 7 tokens</li><li>mean: 11.68 tokens</li><li>max: 17 tokens</li></ul> | <ul><li>min: 23 tokens</li><li>mean: 31.15 tokens</li><li>max: 41 tokens</li></ul> |
* Samples:
  | anchor                             | positive                                                 |
  |:-----------------------------------|:---------------------------------------------------------|
  | <code>오후만 되면 다들 졸아요</code>         | <code>CO2 농도가 1000ppm을 넘으면 졸음과 두통이 늘어나므로 즉시 환기한다.</code> |
  | <code>이산화탄소 몇 ppm부터 환기해야 해?</code> | <code>CO2 농도가 1000ppm을 넘으면 졸음과 두통이 늘어나므로 즉시 환기한다.</code> |
  | <code>교실에서 머리가 지끈거려요</code>        | <code>CO2 농도가 1000ppm을 넘으면 졸음과 두통이 늘어나므로 즉시 환기한다.</code> |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "MultipleNegativesRankingLoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `learning_rate`: 2e-05
- `warmup_steps`: 0.1
- `gradient_accumulation_steps`: 2
- `bf16`: True
- `prompts`: {'anchor': 'task: search result | query: ', 'positive': 'title: none | text: '}
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 8
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 2e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0.1
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 2
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1.0
- `label_smoothing_factor`: 0.0
- `bf16`: True
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 8
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: {'anchor': 'task: search result | query: ', 'positive': 'title: none | text: '}
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
| Epoch  | Step | Training Loss | classroom_cosine_ndcg@10 |
|:------:|:----:|:-------------:|:------------------------:|
| 0.5263 | 10   | 2.2097        | -                        |
| 1.0    | 19   | -             | 0.9342                   |
| 1.0526 | 20   | 1.1344        | -                        |
| 1.5789 | 30   | 0.6073        | -                        |
| 2.0    | 38   | -             | 0.9403                   |
| 2.1053 | 40   | 0.8222        | -                        |
| 2.6316 | 50   | 0.6608        | -                        |
| 3.0    | 57   | -             | 0.9342                   |


### Training Time
- **Training**: 3.9 minutes
- **Evaluation**: 1.8 seconds
- **Total**: 4.0 minutes

### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 6.2.0
- Transformers: 5.20.1
- PyTorch: 2.14.1+cu132
- Accelerate: 1.15.0
- Datasets: 5.1.0
- Tokenizers: 0.23.3

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MatryoshkaLoss
```bibtex
@misc{kusupati2024matryoshka,
    title={Matryoshka Representation Learning},
    author={Aditya Kusupati and Gantavya Bhatt and Aniket Rege and Matthew Wallingford and Aditya Sinha and Vivek Ramanujan and William Howard-Snyder and Kaifeng Chen and Sham Kakade and Prateek Jain and Ali Farhadi},
    year={2024},
    eprint={2205.13147},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->