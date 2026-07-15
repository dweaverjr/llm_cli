## Model family / architecture
- Transformer encoder-only
- Transformer decoder-only (GPT-style)
- Transformer encoder-decoder (T5-style)
- Multimodal transformer
- Vision transformer (ViT)
- Audio transformer
- Speech-to-text encoder-decoder
- Time-series transformer
- Mixture-of-Experts (MoE)
- Mixture-of-Depth
- Recurrent transformer
- State-space models (SSM / Mamba-like)
- Hybrid (Transformer+SSM)
- Retrieval-augmented transformer
- Graph neural network (GNN) + LLM head
- Diffusion-based generative model
- Latent diffusion
- Autoregressive image/video model
- Masked language modeling (BERT-style)
- Prefix-LM / prompt tuning-only model
- Perceiver-style (cross-attn)
- Long-context transformer (sliding window)
- Long-context transformer (global tokens)
- Long-context transformer (segment recurrence)
- Long-context transformer (ring attention)
- Long-context transformer (xformers-style variants)

## Parameterization / scaling
- Dense parameters
- Sparse parameters
- MoE routing
- Tensor parallelism
- Pipeline parallelism
- Data parallelism
- Quantized weights (int8/int4)
- Low-rank adapters (LoRA)
- Prefix-tuning / P-tuning
- Prompt learning (soft prompts)
- Full fine-tune
- Continual learning
- Catastrophic forgetting mitigation
- Knowledge distillation (teacher->student)
- Self-distillation
- Quantization-aware training

## Attention / context handling
- Full attention
- Causal attention
- Bidirectional attention
- Sliding window attention
- Block sparse attention
- Local attention + global tokens
- Rotary position embeddings (RoPE)
- Learned absolute positional embeddings
- ALiBi positional bias
- Relative position bias
- Position interpolation
- Position extrapolation
- Context packing
- Context window extension via training
- KV cache
- KV cache compression
- Attention sink tokens
- Retrieval + attention fusion

## Tokenization / text representation
- Wordpiece tokenizer
- BPE tokenizer
- Unigram tokenizer
- SentencePiece
- Byte-level BPE
- Character-level
- Unnormalized byte tokens
- Special tokens (BOS/EOS/CLS)
- Chat template tokens
- Tool/function call tokens
- Structured output tokens (JSON mode style)

## Training objectives
- Next-token prediction (AR LM)
- Masked token prediction (MLM)
- Denoising objective (seq2seq denoise)
- Contrastive learning (CLIP-style)
- Contrastive span prediction
- Language modeling + auxiliary losses
- Reinforcement learning from human feedback (RLHF)
- Direct Preference Optimization (DPO)
- Odds-ratio optimization
- Reward modeling
- Policy gradient (PPO-style)
- Self-play training
- Goal-conditioned training
- Curriculum learning
- Supervised fine-tuning (SFT)
- Instruction tuning

## Alignment / optimization
- Reward model training
- RLHF (PPO)
- RLHF (variant)
- DPO
- IPO-style optimization
- Calibration / logit adjustment
- Safety fine-tuning
- Preference calibration
- Refusal tuning
- Constitutional AI style
- Chain-of-thought supervision (where used)
- Outcome-based training
- Human feedback aggregation

## Sampling / decoding
- Greedy decode
- Temperature sampling
- Top-k sampling
- Nucleus sampling (top-p)
- Typical sampling
- Min-p sampling
- Beam search
- Diverse beam search
- Length penalty
- Repetition penalty
- No-repeat ngram
- Stop sequences
- Logit biasing
- Speculative decoding
- Assisted decoding
- Contrastive decoding

## Inference acceleration
- KV cache reuse
- FlashAttention
- FlashAttention-2/3
- CUDA graph capture
- Continuous batching
- Paged attention
- TensorRT-LLM
- Speculative decoding
- Multi-query attention (MQA)
- Grouped-query attention (GQA)
- Sliding KV cache
- Quantized KV cache

## Memory / tools / systems
- Retrieval-augmented generation (RAG)
- Vector database
- Hybrid search (BM25 + vector)
- Reranker models
- Tool/function calling
- Agent loop
- Planner-controller
- State tracking
- Scratchpad / working memory
- Structured memory (entities)
- Long-term memory via summaries
- Episodic memory
- Event extraction memory

## Multimodal concepts
- Image encoder + text decoder
- Video transformer (space-time attention)
- Audio encoder + text decoder
- Cross-attention between modalities
- Late fusion (separate encoders)
- Early fusion (shared stem)
- Modality adapters
- Image tokenization (VQ-VAE tokens)
- Patch embeddings for vision
- Audio spectrogram tokenization

## Evaluation concepts
- Perplexity
- Accuracy on tasks
- MMLU-style evals
- Benchmarks (reasoning, coding, safety)
- Truthfulness / factuality eval
- Hallucination rate metrics
- Calibration metrics
- Robustness to prompt changes
- Toxicity / policy compliance
- Pass@k for code
- Retrieval accuracy / citation faithfulness

## Deployment / runtime
- Context length limits
- Streaming generation
- Token streaming
- Rate limiting
- Batch inference
- Backpressure
- Caching responses
- Model routing (multi-model)
- Fallback models
- Cost-based routing
- Health checks

## Governance / security
- Prompt injection defenses
- Jailbreak resilience
- Output filtering
- Content moderation
- Data retention policies
- Audit logs
- Privacy redaction
- PII handling
- Threat models for tools/agents