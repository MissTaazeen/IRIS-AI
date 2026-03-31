import { useEffect, useState } from "react";
import { fetchAllData, fetchAnalysis } from "./api";

export default function App() {
  const [data, setData] = useState(null);
  const [analysis, setAnalysis] = useState(null);

  const [loadingData, setLoadingData] = useState(true);
  const [loadingAnalysis, setLoadingAnalysis] = useState(true);

  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch base data (fast)
    fetchAllData()
      .then(res => setData(res))
      .catch(err => setError(err.message))
      .finally(() => setLoadingData(false));

    // Fetch AI analysis (slow)
    fetchAnalysis()
      .then(res => setAnalysis(res))
      .catch(err => setError(err.message))
      .finally(() => setLoadingAnalysis(false));
  }, []);

  return (
    <div className="min-h-screen bg-[#0f172a] text-white p-6">
      <h1 className="text-3xl font-bold mb-6">
        IRIS - India Risk Intelligence
      </h1>

      {/* ERROR */}
      {error && (
        <div className="bg-red-500 p-3 rounded mb-4">
          {error}
        </div>
      )}

      {/* DATA SECTION */}
      <div className="mb-6">
        <h2 className="text-xl mb-2">Live Data</h2>

        {loadingData ? (
          <SkeletonCard />
        ) : (
          <pre className="bg-gray-900 p-3 rounded text-sm overflow-auto max-h-60">
            {JSON.stringify(data, null, 2)}
          </pre>
        )}
      </div>

      {/* ANALYSIS SECTION */}
      <div>
        <h2 className="text-xl mb-2">AI Risk Analysis</h2>

        {loadingAnalysis ? (
          <LoadingAnalysis />
        ) : analysis ? (
          <AnalysisCard analysis={analysis} />
        ) : null}
      </div>
    </div>
  );
}

function SkeletonCard() {
  return (
    <div className="animate-pulse bg-gray-800 p-4 rounded">
      <div className="h-4 bg-gray-600 mb-2 w-1/3"></div>
      <div className="h-4 bg-gray-600 mb-2 w-1/2"></div>
      <div className="h-4 bg-gray-600 w-2/3"></div>
    </div>
  );
}

function LoadingAnalysis() {
  return (
    <div className="bg-gray-800 p-4 rounded animate-pulse">
      <p className="text-yellow-400">Analyzing national risk...</p>
    </div>
  );
}

function AnalysisCard({ analysis }) {
  const getColor = (risk) => {
    if (risk < 30) return "text-green-400";
    if (risk < 70) return "text-yellow-400";
    return "text-red-500";
  };

  return (
    <div className="bg-gray-900 p-4 rounded shadow">
      <h3 className={`text-2xl font-bold ${getColor(analysis.risk_index)}`}>
        Risk Index: {analysis.risk_index}
      </h3>

      <p className="mt-2">{analysis.national_brief}</p>

      <div className="mt-3">
        <h4 className="font-semibold">Top Drivers:</h4>
        <ul className="list-disc ml-5">
          {analysis.top_drivers.map((d, i) => (
            <li key={i}>{d}</li>
          ))}
        </ul>
      </div>

      <div className="mt-3">
        <h4 className="font-semibold">Forecast:</h4>
        <ul className="list-disc ml-5">
          {analysis.forecasts.map((f, i) => (
            <li key={i}>{f}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}