import './style.css'

document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
  <div class="flex h-screen bg-[#0b0f1a] text-white">
    
    <!-- Sidebar -->
    <div class="w-64 bg-[#111827] p-4">
      <h1 class="text-xl font-bold mb-4">IRIS-AI 🇮🇳</h1>
      <p class="text-sm text-gray-400">India Risk Intelligence</p>
    </div>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col">
      
      <!-- Topbar -->
      <div class="p-4 border-b border-gray-800 flex justify-between">
        <span>Dashboard</span>
        <span class="text-green-400">● LIVE</span>
      </div>

      <!-- Map Area -->
      <div class="flex-1 flex items-center justify-center">
        <h2 class="text-2xl text-gray-400">Map Loading...</h2>
      </div>

    </div>

  </div>
`