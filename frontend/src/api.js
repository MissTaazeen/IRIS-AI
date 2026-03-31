const BASE_URL = "/api";

export async function fetchAllData() {
  const res = await fetch(`${BASE_URL}/data`);
  return res.json();
}

export async function fetchAnalysis() {
  const res = await fetch(`${BASE_URL}/analyze`);
  if (!res.ok) throw new Error("Analysis failed");
  return res.json();
}

export async function fetchMap() {
  const res = await fetch(`${BASE_URL}/map`);
  if (!res.ok) throw new Error("Map fetch failed");
  return res.json();
}