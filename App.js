// EmailSummarizer.jsx
import { useState } from "react";

const GEMINI_KEY = 

async function summarizeEmail(email) {
  const prompt = `You are an email summarizer. Your job is to summarize an email in anywhere between N/2 to N/5 size in terms of number
of words, where N is the total number of words in the email. You may break this limit only if absolutely necessary.

While summarizing, pay special attention to:
1. Classify the email as read-only or not read-only.
2. If it requires a response, classify whether it's a textual response or also requires a file attachment.
3. Summarize using 20% to 50% of the original length, conveying the core message and ideas.

Return ONLY valid JSON in this exact format:
{
  "Read only": true/false,
  "Files required in response": true/false,
  "Summary": "text"
}

The user email:
"""${email}"""`;

  const response = await fetch(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" +
      GEMINI_KEY,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }],
        generationConfig: {
          responseMimeType: "application/json",
          temperature: 0.0,
        },
      }),
    }
  );

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`API error ${response.status}: ${errText}`);
  }

  const data = await response.json();
  const text = data.candidates?.[0]?.content?.parts?.[0]?.text;

  if (!text) {
    throw new Error("No content returned from API");
  }

  const cleaned = text.replace(/```json|```/g, "").trim();
  return JSON.parse(cleaned);
}

export default function EmailSummarizer() {
  const [email, setEmail] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    if (!email.trim()) return;
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const parsed = await summarizeEmail(email);
      setResult(parsed);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="email-summarizer">
      <textarea
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Paste your email here..."
        rows={10}
        className="email-input"
      />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Summarizing..." : "Summarize"}
      </button>

      {error && <p className="error-text">{error}</p>}

      {result && (
        <div className="result-box">
          <p>
            <strong>Read only:</strong> {String(result["Read only"])}
          </p>
          <p>
            <strong>Files required in response:</strong>{" "}
            {String(result["Files required in response"])}
          </p>
          <p>
            <strong>Summary:</strong> {result["Summary"]}
          </p>
        </div>
      )}
    </div>
  );
}