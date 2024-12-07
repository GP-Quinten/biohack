<script lang="ts">
	import '../app.css';
	let { children } = $props();
	import Header from '$lib/components/custom/Header.svelte';
	import { browser } from '$app/environment';

	const drugCandidates = [
		{
			name: 'Memantine',
			confidence: 95,
			status: 'FDA Approved',
			description: "NMDA receptor antagonist approved for moderate to severe Alzheimer's disease."
		},
		{
			name: 'Compound AZ-284',
			confidence: 92,
			status: 'Phase II Clinical Trial',
			description: 'Novel tau protein inhibitor showing promising results in early trials.'
		},
		{
			name: 'Metformin',
			confidence: 87,
			status: 'Repurposing Candidate',
			description:
				'Diabetes medication showing potential neuroprotective effects in preclinical studies.'
		}
	];
</script>

<div class="min-h-screen bg-gray-50">
	<Header />

	<main class="mx-auto max-w-7xl px-4 py-8">
		{@render children()}
	</main>
</div>

<svelte:head>
	{#if browser}
		<script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.0.1/3Dmol-min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.0.1/3Dmol.js"></script>
	{/if}
</svelte:head>
