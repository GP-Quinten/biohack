<script lang="ts">
	import DiseaseSearchPanel from '$lib/components/custom/DiseaseSearchPanel.svelte';
	import DrugCard from '$lib/components/custom/DrugCard.svelte';
	import * as ToggleGroup from '$lib/components/ui/toggle-group/index.js';
	import { fade, fly } from 'svelte/transition';
	import { Star, BookOpenText, Loader2, CirclePlus, ChartSpline } from 'lucide-svelte';
	import Confetti from 'svelte-confetti';

	let selectedModel: 'rating-based' | 'similarity-based' = 'rating-based';
	let selectedSearchAlgorithm: 'greedy' | 'ucb' = 'greedy';
	let isLoading = false;

	let searchQuery: string = 'Alzheimer';

	// When selectedSearchAlgorithm or selectedModel change set isLoading to true during 2s
	// $: if (selectedSearchAlgorithm || selectedModel) {
	// 	isLoading = true;
	// 	setTimeout(() => {
	// 		isLoading = false;
	// 	}, 2000);
	// }
</script>

<div in:fly={{ y: 20, duration: 500 }} class="mb-8">
	<h2 class="text-3xl font-bold text-gray-900">Drug Repurposing Platform</h2>
</div>

<div class="mb-8 grid gap-8">
	<DiseaseSearchPanel bind:searchQuery />
</div>

<div class="mb-8 grid gap-8 md:grid-cols-1">
	<div class="flex flex-col gap-4 rounded-lg bg-white p-6 shadow-lg">
		<div>
			<h2 class="mb-2 text-xl font-semibold">Prediction Modalities</h2>
			<div class="w-full">
				<ToggleGroup.Root
					type="single"
					class="flex w-full flex-row gap-2"
					bind:value={selectedModel}
				>
					<ToggleGroup.Item value="rating-based" aria-label="Rating Based" class="h-32 w-full">
						<Star class="h-4 w-4" />
						Rating Based
					</ToggleGroup.Item>
					<ToggleGroup.Item
						value="similarity-based"
						aria-label="Similarity Based"
						class="h-32 w-full"
						disabled
					>
						<BookOpenText class="h-4 w-4" />
						Include Similarity Based
					</ToggleGroup.Item>
				</ToggleGroup.Root>
			</div>
		</div>
		<div>
			<h2 class="mb-2 text-xl font-semibold">Search Algorithms</h2>
			<div class="w-full">
				<ToggleGroup.Root
					type="single"
					class="flex w-full flex-row gap-2"
					bind:value={selectedSearchAlgorithm}
				>
					<ToggleGroup.Item value="greedy" aria-label="Greedy Search" class="h-32 w-full">
						<CirclePlus class="h-4 w-4" />
						Greedy Search
					</ToggleGroup.Item>
					<ToggleGroup.Item value="ucb" aria-label="UCB Search" class="h-32 w-full">
						<ChartSpline class="h-4 w-4" />
						UCB Search
					</ToggleGroup.Item>
				</ToggleGroup.Root>
			</div>
		</div>
	</div>
</div>

{#if searchQuery}
	<div class="mb-6">
		<h3 class="mb-2 text-2xl font-semibold text-gray-900">Drug Candidates for {searchQuery}</h3>
		<p class="text-gray-600">Including approved drugs and repurposing candidates</p>
	</div>

	<div class="min-h-[600px] w-full">
		{#if isLoading}
			<div class="flex h-full items-center justify-center">
				<Loader2 class="h-10 w-10 animate-spin text-gray-600" />
			</div>
		{:else if selectedSearchAlgorithm === 'greedy'}
			<!-- Harcoded because too lazy to fetch from API :( -->
			<div class="flex h-full items-center justify-center">
				<Confetti rounded size={15} />
			</div>
			<div transition:fly={{ y: 20, duration: 500 }} class="grid gap-6 md:grid-cols-3">
				<DrugCard
					drugDetails={{
						name: 'Methotrexate',
						confidence: 0.78,
						status: 'FDA Approved',
						description:
							'Methotrexate is an antineoplastic agent used to treat various cancers, severe psoriasis, and rheumatoid arthritis by inhibiting nucleotide synthesis enzymes.',
						drugbank_id: 'DB00563',
						pubchem_cid: '126941',
						molecularWeight: 454.44,
						logP: -1.85,
						hydrogenBondDonors: 5,
						hydrogenBondAcceptors: 11,
						mechanism:
							'Methotrexate inhibits dihydrofolate reductase, blocking the synthesis of nucleotides necessary for DNA and RNA replication, leading to reduced inflammation and cancer cell proliferation.',
						toxicity:
							'Methotrexate has a narrow therapeutic index with potential side effects such as bone marrow suppression, gastrointestinal irritation, and hepatotoxicity.',
						halfLife: '3-15 hours (dose-dependent)',
						bioavailability: '64-90% (oral doses up to 25mg)',
						routeOfAdministration: ['Oral', 'Intramuscular', 'Intravenous', 'Subcutaneous'],
						absorption:
							'Highly absorbed through oral administration, though bioavailability decreases with higher doses due to carrier saturation.',
						distribution: 'Widely distributed in body fluids; protein binding of 46-54%.',
						metabolism:
							'Primarily metabolized in the liver and tissues to methotrexate polyglutamates; some conversion to 7-hydroxymethotrexate.',
						elimination:
							'Excreted mainly through urine (~80% unchanged); some excretion occurs via bile.',
						patents: ['US20210323654', 'US20210323655', 'US7891011', 'US6547892'],
						interactions: [
							{
								drug: 'Abacavir',
								severity: 'Moderate',
								effect: 'May decrease excretion, raising serum levels.'
							},
							{
								drug: 'Abatacept',
								severity: 'Moderate',
								effect: 'May increase methotrexate metabolism.'
							}
						],
						sideEffects: [
							{ effect: 'Nausea', frequency: 'Common', severity: 'Mild' },
							{ effect: 'Mucosal ulceration', frequency: 'Occasional', severity: 'Moderate' },
							{ effect: 'Hepatotoxicity', frequency: 'Rare', severity: 'Severe' }
						],
						trials: [
							{ phase: 'Phase 2', status: 'Active', condition: 'Rheumatoid Arthritis' },
							{ phase: 'Phase 3', status: 'Completed', condition: 'Acute Lymphoblastic Leukemia' }
						],
						psa: 210.94,
						rotableBonds: 8,
						therapeuticClass: ['Antimetabolite', 'Antineoplastic Agent', 'Immunosuppressant']
					}}
				/>
				<DrugCard
					drugDetails={{
						name: 'Cyproheptadine',
						confidence: 0.5955,
						status: 'FDA Approved',
						description:
							'Cyproheptadine is an antihistamine and serotonin antagonist used to treat allergic reactions, stimulate appetite, and manage serotonin syndrome off-label.',
						drugbank_id: 'DB00434',
						pubchem_cid: '2911',
						molecularWeight: 287.4,
						logP: 3.6,
						hydrogenBondDonors: 0,
						hydrogenBondAcceptors: 1,
						mechanism:
							'Cyproheptadine acts as a competitive antagonist of histamine H1 receptors and serotonin receptors (5-HT2A, 5-HT2C), reducing allergy symptoms and stimulating appetite by influencing the hypothalamus.',
						toxicity:
							'Overdose may cause sedation, dry mouth, flushing, and anticholinergic side effects. Severe cases can involve CNS stimulation in children or hypotension.',
						halfLife: 'Not Available',
						bioavailability: 'High (oral)',
						routeOfAdministration: ['Oral'],
						absorption:
							'Well-absorbed orally with a mean Tmax of 4 hours; sublingual administration is slower with reduced bioavailability.',
						distribution: 'Widely distributed; precise protein binding data not available.',
						metabolism:
							'Primarily metabolized into a quaternary ammonium glucuronide conjugate, excreted in urine and feces.',
						elimination:
							'40% excreted in urine; 2-20% excreted in feces, with about 34% as unchanged drug.',
						patents: [],
						interactions: [
							{
								drug: 'Epinephrine',
								severity: 'Moderate',
								effect: 'Used adjunctively in anaphylaxis management.'
							}
						],
						sideEffects: [
							{ effect: 'Drowsiness', frequency: 'Common', severity: 'Mild' },
							{ effect: 'Dry mouth', frequency: 'Common', severity: 'Mild' },
							{ effect: 'Flushing', frequency: 'Occasional', severity: 'Moderate' }
						],
						trials: [
							{ phase: 'Phase 2', status: 'Completed', condition: 'Allergic Reactions' },
							{ phase: 'Phase 4', status: 'Completed', condition: 'Appetite Stimulation' }
						],
						psa: 12.47,
						rotableBonds: 1,
						therapeuticClass: ['Antihistamine', 'Serotonin Antagonist']
					}}
				/>
				<DrugCard
					drugDetails={{
						name: 'Mitoxantrone',
						confidence: 0.4224,
						status: 'FDA Approved',
						description:
							'Mitoxantrone is a topoisomerase inhibitor used to treat multiple sclerosis and various cancers by interfering with DNA replication and repair.',
						drugbank_id: 'DB01204',
						pubchem_cid: '4212',
						molecularWeight: 444.48,
						logP: -0.4,
						hydrogenBondDonors: 4,
						hydrogenBondAcceptors: 8,
						mechanism:
							'Mitoxantrone intercalates into DNA, causing crosslinks and strand breaks. It inhibits topoisomerase II, preventing DNA replication and repair, leading to apoptosis of rapidly dividing cells.',
						toxicity:
							'Mitoxantrone can cause severe leukopenia, leading to increased infection risk, and may also result in cardiotoxicity and hepatotoxicity with cumulative doses.',
						halfLife: '75 hours',
						bioavailability: 'Poor (oral); administered intravenously.',
						routeOfAdministration: ['Intravenous'],
						absorption:
							'Poor oral absorption; typically administered intravenously for optimal bioavailability.',
						distribution:
							'Extensive (Volume of Distribution: 1000 L/m²); 78% plasma protein binding.',
						metabolism:
							'Primarily metabolized in the liver. The main metabolite is mitoxantrone glucuronide.',
						elimination: 'Exact route not well defined; partial renal and hepatic clearance.',
						patents: [],
						interactions: [
							{
								drug: 'Abatacept',
								severity: 'Moderate',
								effect: 'Increases adverse effect risk.'
							},
							{
								drug: 'Abemaciclib',
								severity: 'Moderate',
								effect: 'May reduce mitoxantrone excretion, increasing serum levels.'
							}
						],
						sideEffects: [
							{ effect: 'Leukopenia', frequency: 'Common', severity: 'Severe' },
							{ effect: 'Nausea', frequency: 'Common', severity: 'Mild' },
							{ effect: 'Cardiotoxicity', frequency: 'Occasional', severity: 'Severe' }
						],
						trials: [
							{ phase: 'Phase 2', status: 'Completed', condition: 'Multiple Sclerosis' },
							{ phase: 'Phase 3', status: 'Active', condition: 'Acute Myeloid Leukemia' }
						],
						psa: 104.1,
						rotableBonds: 4,
						therapeuticClass: ['Topoisomerase Inhibitor', 'Antineoplastic Agent']
					}}
				/>
				<DrugCard
					drugDetails={{
						name: 'Pheniramine',
						confidence: 0.3972,
						status: 'FDA Approved',
						description:
							'Pheniramine is a first-generation antihistamine used to treat allergy symptoms such as hay fever, pruritus, and allergic conjunctivitis by blocking histamine receptors.',
						drugbank_id: 'DB01620',
						pubchem_cid: '4760',
						molecularWeight: 240.34,
						logP: 2.9,
						hydrogenBondDonors: 0,
						hydrogenBondAcceptors: 2,
						mechanism:
							'Pheniramine acts as an inverse agonist at histamine H1 and H4 receptors, reducing allergic symptoms by blocking histamine-induced vasodilation, itching, and swelling.',
						toxicity:
							'Overdose can cause QTc prolongation, arrhythmias, and central nervous system depression. Activated charcoal is effective in reducing absorption in overdose cases.',
						halfLife: '8-17 hours',
						bioavailability: 'High (oral)',
						routeOfAdministration: ['Oral', 'Intravenous', 'Intramuscular', 'Ophthalmic'],
						absorption:
							'Well-absorbed orally with a Tmax of 1-2.5 hours and a Cmax ranging from 173-294 ng/mL after a 30.5 mg dose.',
						distribution: 'Wide tissue distribution; specific protein binding data not available.',
						metabolism:
							'Primarily metabolized through N-dealkylation into N-didesmethylpheniramine and N-desmethylpheniramine.',
						elimination:
							'Eliminated via renal excretion, with 24.3% of the drug excreted unchanged in urine.',
						patents: [],
						interactions: [
							{
								drug: 'Acrivastine',
								severity: 'Moderate',
								effect: 'May increase the risk of QTc prolongation.'
							},
							{
								drug: 'Adenosine',
								severity: 'Moderate',
								effect: 'May increase QTc prolongation risk.'
							}
						],
						sideEffects: [
							{ effect: 'Drowsiness', frequency: 'Common', severity: 'Mild' },
							{ effect: 'Dry mouth', frequency: 'Occasional', severity: 'Moderate' },
							{ effect: 'Arrhythmias', frequency: 'Rare', severity: 'Severe' }
						],
						trials: [
							{ phase: 'Phase 3', status: 'Completed', condition: 'Allergic Rhinitis' },
							{ phase: 'Phase 4', status: 'Completed', condition: 'Pruritus' }
						],
						psa: 16.1,
						rotableBonds: 3,
						therapeuticClass: ['Antihistamine', 'Anti-Allergic Agent', 'Antipruritic']
					}}
				/>
			</div>
		{:else if selectedSearchAlgorithm === 'ucb'}
			<div transition:fly={{ y: 20, duration: 500 }} class="grid gap-6 md:grid-cols-3">
				<div class="flex flex-col gap-6 rounded-md border-2 border-blue-300 bg-blue-200 p-3">
					<div class="flex w-full items-center justify-center">
						<!-- Badge groupe 1 -->
						<span
							class="flex h-10 w-10 items-center justify-center rounded-full border-2 border-blue-500 bg-blue-500 px-2 py-1 text-xl text-white"
							>1</span
						>
					</div>
					<DrugCard />
					<DrugCard />
					<DrugCard />
				</div>
				<div class="flex flex-col gap-6 rounded-md border-2 border-red-300 bg-red-200 p-3">
					<div class="flex w-full items-center justify-center">
						<!-- Badge groupe 2 -->
						<span
							class="flex h-10 w-10 items-center justify-center rounded-full border-2 border-red-500 bg-red-500 px-2 py-1 text-xl text-white"
							>2</span
						>
					</div>
					<DrugCard />
					<DrugCard />
					<DrugCard />
				</div>
				<div class="flex flex-col gap-6 rounded-md border-2 border-yellow-300 bg-yellow-200 p-3">
					<div class="flex w-full items-center justify-center">
						<!-- Badge groupe 3 -->
						<span
							class="flex h-10 w-10 items-center justify-center rounded-full border-2 border-yellow-500 bg-yellow-500 px-2 py-1 text-xl text-white"
							>3</span
						>
					</div>
					<DrugCard />
					<DrugCard />
					<DrugCard />
				</div>
			</div>
		{/if}
	</div>
{/if}
