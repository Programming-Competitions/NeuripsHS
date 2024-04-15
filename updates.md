# Updates over time

Apr 13:
 - decided on this idea
 - got started on the translation model, collecting data
 - fired up the CulturaX base pipeline

Apr 14:
 - finished collecting full subsets all indian languages, except partial subsets of hindi and english, both around ~15gb
 - will start looking into collecting the translation data in hplt and the aya datasets, and maybe opus/xp3
 - looking at a llama2c base model or t5, but LLama2c is easier to deal with at size, will probably mix all the data together (or use doremi/doge), and then train a 50m-100m model
 - looking into finetuning whisper base/small (74m/224m), finetuned on probably ~400hrs of data heavily biased with tone/dialect for good indian subcontinent language transcription
 - the lallantop youtube channel scraped, along with a couple other sources is probably good enough, most of their videos come with transcripts, and they have well over ~400hrs of content, spread across multiple indian states
 - other than that just scrape the millions of indian village youtubers, most of them are content farms with several hundred hours again, and theres like a couple good ones per state/language to scrape from
