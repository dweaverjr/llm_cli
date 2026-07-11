# OpenAI Model Reference

## Flagship Chat / Reasoning Models

| Model | Best Used For |
|---|---|
| `gpt-5.5-pro`, `gpt-5.5` | Latest top-tier general reasoning, coding, complex multi-step tasks. Pro = highest quality/slower/costlier. |
| `gpt-5.4`, `gpt-5.4-pro` | Prior-gen flagship, strong reasoning + coding; pro variant for max quality. |
| `gpt-5.4-mini`, `gpt-5.4-nano` | Cheaper/faster versions of 5.4 for lightweight chat, simple tasks, high-volume apps. |
| `gpt-5.2`, `gpt-5.2-pro`, `gpt-5.1`, `gpt-5`, `gpt-5-mini`, `gpt-5-nano` | Earlier GPT-5 generation snapshots; general-purpose chat/reasoning at varying cost/speed tiers. |
| `gpt-5-chat-latest`, `gpt-5.1-chat-latest`, `gpt-5.2-chat-latest`, `gpt-5.3-chat-latest` | Rolling "latest" aliases tuned for conversational ChatGPT-style use; auto-updates to newest chat model. |
| `chat-latest` | Generic rolling alias to newest chat-optimized model — good default when you don't want to track versions. |
| `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano` | Long-context (1M token) GPT-4 gen; mini/nano for cost-sensitive high-throughput use. |
| `gpt-4o`, `gpt-4o-mini` | Multimodal (text/image/audio) workhorse; mini for cheap/fast simple tasks. |
| `gpt-4-turbo`, `gpt-4`, `gpt-4-0613` | Legacy GPT-4 — keep only for backward compatibility with old prompts/behavior. |
| `gpt-3.5-turbo`, `gpt-3.5-turbo-16k`, `gpt-3.5-turbo-instruct` | Legacy low-cost chat/completion; superseded by 4o-mini/5-nano, mainly legacy support. |

## Reasoning ("o-series") Models

| Model | Best Used For |
|---|---|
| `o3`, `o3-mini` | Deep reasoning for math, coding, planning tasks needing chain-of-thought; mini = cheaper/faster. |
| `o4-mini` | Efficient reasoning model, good reasoning/cost tradeoff for coding & STEM tasks. |
| `o1`, `o1-pro` | Earlier reasoning-focused models; pro = higher effort/quality reasoning at higher cost. |

## Coding-Specialized

| Model | Best Used For |
|---|---|
| `gpt-5.1-codex`, `gpt-5.1-codex-mini`, `gpt-5.1-codex-max`, `gpt-5.2-codex`, `gpt-5.3-codex`, `gpt-5-codex` | Agentic coding tasks — repo-aware code generation, editing, terminal/tool use (e.g., Copilot/CLI agents). |

## Image Generation

| Model | Best Used For |
|---|---|
| `gpt-image-2`, `gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini` | Text-to-image generation/editing; mini = cheaper/faster, lower fidelity. |
| `chatgpt-image-latest` | Rolling alias for ChatGPT's current image model. |

## Audio: Speech-to-Text (Transcription)

| Model | Best Used For |
|---|---|
| `whisper-1` | General-purpose, robust multilingual transcription (classic baseline). |
| `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` | Higher-accuracy transcription with better context handling; mini = cheaper. |
| `gpt-4o-transcribe-diarize` | Transcription with speaker diarization (who-said-what). |

## Audio: Text-to-Speech

| Model | Best Used For |
|---|---|
| `tts-1` | Fast, low-latency speech synthesis. |
| `tts-1-hd` | Higher-quality/more natural voice synthesis, less latency-sensitive use. |
| `gpt-4o-mini-tts` | Instructable TTS (control tone/style via prompt), cheap. |

## Audio: Realtime / Voice Conversation

| Model | Best Used For |
|---|---|
| `gpt-realtime`, `gpt-realtime-2`, `gpt-realtime-1.5`, `gpt-realtime-mini` | Low-latency streaming voice conversations (voice assistants, live agents). |
| `gpt-realtime-whisper` | Realtime speech recognition variant for streaming transcription. |
| `gpt-realtime-translate` | Realtime speech-to-speech/text translation. |
| `gpt-audio`, `gpt-audio-mini`, `gpt-audio-1.5` | General audio-in/audio-out model for non-realtime audio conversation tasks. |

## Video Generation

| Model | Best Used For |
|---|---|
| `sora-2`, `sora-2-pro` | Text/image-to-video generation; pro = higher quality/longer/more expensive. |

## Embeddings

| Model | Best Used For |
|---|---|
| `text-embedding-3-small` | Cheap, fast embeddings for semantic search/RAG at scale. |
| `text-embedding-3-large` | Higher-accuracy embeddings when retrieval quality matters more than cost. |
| `text-embedding-ada-002` | Legacy embedding model, kept for compatibility. |

## Moderation

| Model | Best Used For |
|---|---|
| `omni-moderation-latest` | Classify content (text/image) for policy violations — safety filtering pipelines. |

## Search-Augmented

| Model | Best Used For |
|---|---|
| `gpt-4o-mini-search-preview`, `gpt-4o-search-preview` | Chat with built-in web search grounding for up-to-date answers. |
| `gpt-5-search-api` | API-oriented search-augmented generation. |

## Legacy Base / Completion Models

| Model | Best Used For |
|---|---|
| `davinci-002`, `babbage-002` | Legacy raw completion (non-chat) models; fine-tuning base or simple completions. babbage = cheaper/smaller. |

---

### Notes
- Dated suffixes (e.g. `-2025-08-07`) = pinned snapshot for reproducibility; undated name = auto-updating alias.
- For production, pin to a dated snapshot to avoid silent behavior changes.
- `owned_by='system'` vs `'openai-internal'` vs `'openai'` reflects internal OpenAI categorization, not functional difference.
