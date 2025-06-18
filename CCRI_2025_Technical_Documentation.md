# Children’s Climate Risk Index (CCRI) 2025

# Technical Documentation

# -DRAFT-

Last updated: 24 April 2025

Climate and Environment Data Unit

Division of Data, Analytics, Planning and Monitoring

## UNICEF HQ

# Contents

- Background................................................................................................................................................. 3
- Overview...................................................................................................................................................... 3
- Theoretical Framework............................................................................................................................ 3
- What is new in CCRI 2025?..................................................................................................................... 4
- What is not included in CCRI 2025?........................................................................................................4
- Section 1: Data Selection...........................................................................................................................5
- - Pillar 1 – Children’s Exposure to Hazards...................................................................................................5
- - Flood........................................................................................................................................................ 7
- Drought.................................................................................................................................................... 8
- Tropical Storms...................................................................................................................................... 10
- Heat....................................................................................................................................................... 11
- Sand and Dust Storms...........................................................................................................................12
- Fires.......................................................................................................................................................13
- Air Pollution............................................................................................................................................14
- Vector borne diseases........................................................................................................................... 15

Pillar 2 – Child Vulnerability.......................................................................................................................16

Section 2: Methodology.............................................................................................................................22

- - Data collection and cleaning..................................................................................................................22
- Thresholding.......................................................................................................................................... 22
- Overlay and Summarizing.....................................................................................................................23
- Normalization.........................................................................................................................................23
- Aggregation........................................................................................................................................... 25
- Correlation............................................................................................................................................. 26
- Composite Index....................................................................................................................................26
- Pixel-level multi-hazard Children Climate Risk Index.............................................................................27

Section 4: Results and Interpretation.........................................................................................................33

- Section 5: Policy and Research Implications.............................................................................................33
- Section 6: Disclaimers............................................................................................................................... 33

---

# Appendix

# Background

The planetary crisis of climate change, environmental pollution and biodiversity loss has put virtually every child in the world at risk. We know that children are the least responsible for this global emergency, yet they shoulder the greatest burden of its impact.

In 2021, UNICEF released the first global Children Climate Risk Index (CCRI) that identified the countries that are most-at risk for both climate and environmental hazards – estimating that one billion children live in countries facing extreme risks to their ability to survive, grow and thrive. In 2023, UNICEF released the Sustainability and Climate Change Action Plan (SCAP) galvanizing a global commitment to ensure a sustainable world and protect the most vulnerable children and in 2024 a new Climate and Environment data unit was established to enable easy access to data, analysis for global, regional and country-level applications by developing a global hazard database and updating CCRI. Following extensive internal and external consultations the global CCRI was revised and updated using the best available global hazard and vulnerability data to better understand the extent of vulnerable children’s exposure to climate and climate-sensitive hazards.

# Overview

The Children Climate Risk Index (CCRI) is a composite index that aims to rank countries where vulnerable children are also exposed to a wide range of climate and environmental hazards. Recognizing that children are disproportionately affected by these hazards, CCRI provides a comprehensive assessment of how climate and environmental hazards intersect with children’s existing vulnerabilities. CCRI 2025 adopted the hazard x exposure x vulnerability as the foundational risk framework (IPCC, 2020).

Risk refers to the potential of adverse consequences, resulting from dynamic interactions between climate-related hazards with the exposure and vulnerability of children or associated assets and systems to the hazards.

Hazards refer to the potential occurrence of climate and climate-sensitive hazards that can cause adverse effects to children.

Exposure refers to presence of children that could be adversely affected by hazards.

Vulnerability refers to existing deprivations that are specific to children.

Hazards, exposure and vulnerability may each be subject to uncertainty in terms of magnitude and likelihood of occurrence, and each may change over time and space due to socio-economic changes and human decision-making.

# Theoretical Framework

CCRI 2025, similar to the earlier version, summarizes risk analysis into two critical pillars with components, sub-components and indicators:

Pillar 1 looks at children’s exposure to climate hazards such as riverine and coastal floods, tropical storms, droughts, heatwaves, sand & dust storms, fires and climate-sensitive hazards such as air pollution and vector borne diseases.

Pillar 2 considers the inherent vulnerabilities of children in WASH, nutrition, protection, health, education, poverty and child survival.

## By integrating the two pillars, CCRI provides a powerful framework to understand the specific risks that children face. Understanding these complex interactions is crucial to better prepare, mitigate and adapt to the rapidly evolving climate crisis. This data-driven tool is aimed to allow UNICEF country offices, policy.

makers, humanitarian organizations, and other relevant stakeholders to advocate, prioritize action and allocate resources effectively to protect the most vulnerable children, building a climate resilient future for all. Work is underway to develop global indicators for monitoring adaptation to climate change1 and these could potentially be included as a third pillar in future iterations of CCRI.

# Children's Climate Risk Index 2025

| Children's Exposure to Hazards | Child Vulnerability |
| ------------------------------ | ------------------- |
| 7                              | 1₁                  |

Fig 1: CCRI 2025 Theoretical Framework

# What is new in CCRI 2025?

CCRI 2025 focuses more on climate and climate-sensitive hazards whereas CCRI 2021 included a mix of climate and environmental hazards. Since the list of hazards and the underlying datasets are different, the two indices are not comparable.

CCRI 2025 also estimates the index by country as well as gridded analysis, pinpointing the hotspot areas where vulnerable children are exposed to multiple extreme hazard events in all countries.

CCRI 2025 includes the Small Island Developing States (SIDS) which were omitted from CCRI 2021 due to lack of data availability at that time.

CCRI 2025 also regroups sub-components of the child vulnerability pillar to align with UNICEF programmes, making poverty and child survival as separate components, as well as splitting health and nutrition into separate components.

# What is not included in CCRI 2025?

CCRI 2025 does not attribute to anthropogenic climate hazards but identifies children’s exposure to all hazards. In other words, it is not quantifying the impact of human-induced climate change on children separately from naturally occurring extreme weather events.

## 1 https://unfccc.int/topics/adaptation-and-resilience/workstreams/gga#tab_home

CCRI 2025 does not look at how climate and climate-sensitive hazards increases vulnerability but at where vulnerable children are exposed to these hazards.

CCRI 2025 does not include analysis on future projections of climate risks on children, given the uncertainty in available projections and child population. There are no reliable, modelled estimates available for future child vulnerability.

CCRI 2025 does not include all the possible relevant indicators on climate and climate-sensitive hazards, only those for which open, quantifiable, spatially distributed global data are available.

CCRI 2025 does not include any predictions.

# How to interpret CCRI 2025?

to be included both for composite index and the pixel-based analysis

# Section 1: Data Selection

Multiple data sources were considered and carefully evaluated for each indicator. The final selection is identified based on the following pre-established criteria:

- All input data must be Open source
- Global
- Quantifiable
- Comparable
- Spatially distributed
- Child centric

Proxy indicators are considered where data is not available.

Quality dimension of basic data is considered to maximize the overall quality of the final CCRI, and within the constraints of data availability and include their relevance, accuracy, timeliness, accessibility, interpretability and coherence (OECD, 2008).

# Pillar 1 – Children’s Exposure to Hazards

In CCRI 2025, climate and climate-sensitive hazards refer to those hazards that are directly or indirectly influenced by Earth’s climate system. There is no universal classification available, and the following definitions are adopted for the purpose of CCRI 2025.

Climate hazard refers to natural events that are pre-dominantly hydro-meteorological in nature such as floods, tropical storms, heatwaves, wildfires and droughts. These hazards can be exacerbated by climate change, leading to increased frequency, intensity, and unpredictability (IPCC, 2022).

Climate sensitive hazard refers to hazards such as air pollution and vector borne diseases that are sensitive to changes in climate patterns, such as temperature and precipitation, which can affect the distribution and intensity of these risks (IPCC, 2022).

Understanding climate hazards is core to risk analysis, emergency preparedness and planning for effective mitigation and adaptation. Pillar 1 combines children’s exposure to multiple hazards where open, global data was available. Please note that the list of climate and climate-sensitive hazards is not comprehensive, and other relevant hazards might not have been included due to lack of global data availability.

# Data criteria:

## Probabilistic models were given higher priority to define hazards that could potentially happen at any given point at any given time.

A 100-year return period is considered as default which signifies an event that is both probable, impactful, and likely to happen within a child’s lifetime. Where there is a lack of probabilistic models, long-term observation data has been chosen as a proxy to estimate both the absolute and relative children exposure. The number of years considered varies from hazard to hazard, depending on the data availability and to compensate for the influence of climate change. It is to note that the estimates include all children who could potentially be exposed to a particular hazard and do not account for exposure in any particular year.

# Children Population data:

WorldPop’s global gridded children population estimate (Under 18) for 2024 at 100m spatial resolution was used for all exposure analysis in CCRI 2025. The constrained population data product was used. Individual country population data is first downloaded and mosaicked into a single, global composite layer for further processing. Worldpop is chosen for its higher resolution, global availability and as it has the least bias in estimating rural population (Ritter, 2025).

# Components of Pillar 1:

Pillar 1 of CCRI 2025 includes 10 components with 30 indicators.

1. Flood – Riverine
2. Flood – Coastal
3. Drought – Agricultural
4. Drought – Meteorological
5. Tropical Storm
6. Heatwaves
7. Sand and Dust Storm
8. Fire
9. Air Pollution
10. Vector-Borne Diseases

---

# Exasuresto 3

Refer to the CCRI Data catalog to download the full metadata for all hazard layers.

# Flood

Floods are the natural hazard with the highest frequency and widest geographic distribution (UNISDR, 2017) and are described in terms of frequency and intensity (water extent and depth). There are three common types of flooding.

- Fluvial (riverine)
- Coastal (storm surge / sea level rise)
- Pluvial (surface water / flash floods)

# Relevance:

Floods are a critical concern in climate change discussions due to their widespread impact on human and natural systems. According to the IPCC 2022 AR 6 report, food risks and societal damages are projected to increase with every increment of global warming (medium confidence) (IPCC, 2022). They exacerbate existing vulnerabilities, particularly in communities already facing socioeconomic challenges. Children are especially vulnerable to the impacts of floods. Floods can disrupt their access to clean water, sanitation, and healthcare, leading to increased risks of diseases. Additionally, floods can cause significant psychological stress and trauma, affecting children's mental health and development (IPCC, 2022).

# Fluvial Flood

A fluvial or riverine flood is a rise, usually brief, in the water level of a stream or water body to a peak from which the water level recedes at a slower rate (WMO, 2012). The primary cause of a fluvial flood is an extended precipitation event that occurs at, or upstream from, the affected area and can also occur when traditional flood-control structures, such as levees and dikes, are overtopped.

# Data source:

---

# Fluvial Flood

Fluvial flood has been extensively studied, and multiple global models are freely available at different return periods. For CCRI 2025, JRC’s gridded Global Flood Hazard model (Baugh, 2024) at 100-year return period and 90m spatial resolution has been chosen and water depth above 1cm (defined as data pixel value greater than or equal to in our processing pipeline) has been considered for exposure analysis.

# Data processing:

Children’s exposure to riverine flood hazard was calculated by simple overlay of the flood hazard and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicators:

- Absolute number of children exposed to riverine floods
- Relative number of children exposed to riverine floods

# Data limitations:

While major riverine floods have been modelled at higher resolution, data might not cover smaller rivers.

# Coastal Flood

Coastal flooding is most frequently the result of storm surges and high winds coinciding with high tides (WMO, 2011).

# Data source:

A few open, global coastal flood models were compared at different return periods. For the purpose of CCRI 2025, JRC’s gridded Global Coastal Flood Hazard model at 100-year return period and 90m spatial resolution has been chosen. This is a binary layer, and all values identified as 1 are considered for exposure analysis.

# Data processing:

Children’s exposure to coastal flood hazard was calculated by simple overlay of the flood hazard and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics. Coastal flood does not have any thresholding, it is a binary 0, 1 non-presence or presence of flood used to calculate exposure.

# Coverage:

Global

# Indicators:

- Absolute number of children exposed to coastal floods
- Relative number of children exposed to coastal floods

# Data limitations:

JRC’s coastal flood hazard layer does not include intensity (depth) information, which could be crucial to better estimate the exposure to different impacts on children.

# Pluvial Flood

---

# Definition

A pluvial flood is caused by heavy rainfall that creates a flood independent of an overflowing water body (WMO, 2021).

# Data source:

Data processing:

Children’s exposure to pluvial flood hazard was calculated by overlaying the flood hazard and the high-resolution gridded global child population layer. No threshold was imposed, i.e., anywhere that the pluvial flood data overlapped with child population was considered exposed. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Data limitations:

# Drought

Drought is a prolonged dry period in the natural climate cycle that can occur anywhere in the world. It is typically a slow on-set phenomenon caused by a lack of rainfall and can occur in four stages that are usually categorized as four drought types.

- Meteorological drought
- Agricultural drought
- Hydrological drought
- Socio-economic drought

# Relevance:

Drought has always been a part of the natural variability of Earth’s climate. Climate change increasingly puts pressure on food production and access, especially in vulnerable regions, and undermines food security and nutrition (WMO, 2012). The increase in the frequency, intensity, and duration of droughts will increase risks to food security (IPCC, 2022). Children are especially impacted by various drought risks. The lack of water can compromise their access to clean drinking water and sanitation, increasing the risk of diseases. Additionally, droughts can lead to food shortages, impacting children's nutrition and overall health. The psychological stress and trauma associated with drought conditions can also affect children's mental health and development (IPCC, 2022).

# Agricultural Drought

Agricultural drought occurs when there is insufficient soil moisture to meet the needs of a particular crop at a particular time (FAO, 2025).

# Data source:

## The Agricultural Stress Index (ASI) facilitates the early identification of cropped land with a high likelihood of water stress (drought). The Index is based on the integration of the Vegetation Health Index (VHI) in two dimensions that are critical in the assessment of a drought event in agriculture: temporal and spatial. The first step is a temporal averaging of the VHI, assessing the intensity and duration of dry periods occurring during the crop cycle at the pixel level. The second step determines the spatial extent of drought events by calculating the percentage of pixels in arable areas with a VHI value below 35 percent (this value was identified as a critical threshold in assessing the extent of drought in previous research by Kogan, 1995). Each administrative area is classified according to the percentage of the affected area to facilitate the quick interpretation of results (FAO, 2025). The average Annual ASI from 1984 - 2023 is used.

# Children's Exposure to Drought

in CCRI 2025 as a proxy as it depicts the percentage of arable land, within an administrative area, that has been affected by drought conditions over the entire cropping season.

# Data processing:

Children’s exposure to agricultural drought was calculated by simple overlay of the areas where the long term average annual ASI with over 50% cropland is affected and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicators:

- Absolute number of children exposed to agricultural droughts
- Relative number of children exposed to agricultural droughts

# Data limitations:

Drought is one of the most complex natural hazards and the impact is felt in places that are in proximity as well as those areas that rely on the food supply. In other words, drought can occur in one place and the impact can be felt anywhere that depends on the crop production, even in adjacent or far away countries. For the lack of better model, CCRI 2025 assumes children living in areas close to the actual location of agricultural drought to be directly affected and does not consider children living in areas that depends on the crop production as their primary food source which is hard to model globally.

# Meteorological Drought

# Definition:

Meteorological drought occurs when dry weather patterns dominate an area, defined by the degree of dryness and the duration of the dry period (WMO, 2021).

# Data source:

The Standardized Precipitation Index (SPI) from the European Copernicus Global Drought Observatory at 5km spatial resolution is used to estimate children’s exposure to meteorological drought. SPI indicates how precipitation deviates from the climatological average over a given accumulation period. The indicator is suitable and is commonly used for detecting and characterizing meteorological drought. The longer accumulation periods are related to persistent droughts and may give information also in terms of agricultural and or hydrological drought. (Copernicus, 2025)

# Data processing:

Children’s exposure to meteorological drought was calculated by simple overlay of the areas where SPI is less than -1 and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicators:

- Absolute number of children exposed to meteorological droughts
- Relative number of children exposed to meteorological droughts

# Data limitations:

## 10

SPI only considers precipitation data and does not account for evapotranspiration. This can limit its effectiveness in capturing the impact of increased temperatures on moisture demand and availability.

# Tropical Storms

A tropical storm is a type of storm system characterized by a low-pressure center, a closed low-level atmospheric circulation, strong winds, and a spiral arrangement of thunderstorms that produce heavy rain (WMO, 2021). Tropical storm classification is adopted from WMO’s guidance where wind speed greater than 63 km/hr is considered as a named tropical storm (WMO, 2023).

# Relevance:

Tropical storms can cause significant damage through high winds, heavy rainfall, and storm surges, leading to flooding, property destruction, and loss of life. Climate change is increasing the intensity and frequency of tropical storms. Warmer sea surface temperatures and higher atmospheric moisture levels contribute to more powerful storms with greater precipitation. This intensification is linked to human-induced greenhouse gas emissions, which have led to observable changes in storm patterns and behaviors (IPCC, 2022). Children are particularly vulnerable to the effects of tropical storms. These events can disrupt their access to clean water, food, and healthcare, increasing the risk of malnutrition and diseases and can lead to psychological trauma.

# Data source:

The tropical cyclone wind data is derived from UNEP GIRI and indicates the mean value of wind velocity for a return period of 100 years. The map has global coverage and a resolution of 6' (~11.1 kilometers at the equator) (CDRI, 2023). The tracks of historical tropical cyclones used in GIRI were obtained from the IBTrACS database and hazard analysis was divided by oceanic basis with different cut off years, based on data availability (GIRI, 2023).

# Data processing:

Children’s exposure to tropical storms was calculated by simple overlay of the areas where the wind speed is over 63 km/hr and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicators:

- Absolute number of children exposed to tropical storms
- Relative number of children exposed to tropical storms

# Data limitations:

The accuracy of the probabilistic hazard model depends on the completeness of historical tropical cyclone data which varies from one ocean to another. Incomplete data can lead to underestimation or overestimation of storm exposure.

# Heat

## A heatwave can be defined as a period where local excess heat accumulates over a sequence of unusually hot days and nights (WMO, 2022). Heatwaves are complex phenomena and at present, there is no universal consensus on a global metric. The specific criteria for what constitute a heatwave can vary by region, but it generally involves temperatures significantly higher than the average for that area and time of year.

# For CCRI 2025

A heatwave is defined as any period of 3-days or more when the maximum temperature each day is in the top 10% of the local 15-day average and the following four dimensions were considered:

- Heatwave frequency refers to the number of heatwaves per year.
- Heatwave duration refers to the total number of days an event lasts.
- Heatwave severity refers to the temperature above the local 15-day average during the heatwave, expressed in degrees Celsius.
- Extremely high temperatures (extremely hot days) - when a day exceeds 35 degrees Celsius.

# Relevance:

Temperature is one of the core indicators to describe climate and there is clear evidence that climate change is raising global temperatures and causing historic heat waves all around the world, with higher frequencies, duration and severity (IPCC, 2022). Children are more vulnerable to the short- and long-term effects, especially from the heat stress caused by exposure to heat waves that can negatively affect health and well-being, especially for infants and young children. Children sweat less per kilogram than adults and have a higher metabolism, which means they get hot quicker. School closures because of heatwaves are becoming increasingly common, leading to negative impact on children’s education.

# Note on heatstress

# Data source:

Temperature input is calculated using daily aggregate temperature data from the ERA5 reanalysis (Muñoz, 2019). ERA5, produced by the Copernicus Climate Change Service (C3S) at ECMWF, is the fifth-generation atmospheric reanalysis of the global climate covering the period from January 1940 to present (ECMWF, 2025). For CCRI 2025, the last ten-year average is considered.

# Data processing:

Children’s exposure to individual dimensions was calculated by simple overlay of the areas where the individual dimension of heatwave is greater than the long-term average and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicators:

- Absolute number of children exposed to heatwave frequency
- Relative number of children exposed to heatwave frequency
- Absolute number of children exposed to heatwave duration
- Relative number of children exposed to heatwave duration
- Absolute number of children exposed to heatwave severity
- Relative number of children exposed to heatwave severity
- Absolute number of children exposed to extreme temperature
- Relative number of children exposed to extreme temperature

# Data limitations:

&lt;Mention SIDS countries once we confirm how to integrate them – Rosa’s VUB study pending&gt;

# Sand and Dust Storms

## Sand and dust storms (SDS) are caused by intense winds over areas of arid soil that pick up large amounts of ground material into the atmosphere. The most significant dust sources globally are

concentrated in arid and semi-arid regions, particularly major deserts such as the Sahara in Africa, the Gobi in Asia, and the Arabian Desert in the Middle East. They originate from natural sources like deserts, dry lake beds, and coastal regions with loose sediment. Human activities exacerbate the problem through construction, agriculture, and poor land management practices that strip vegetation and expose soil to wind erosion. Climate change amplifies the occurrence of sand and dust storms by altering weather patterns and reducing vegetation cover. (WMO, 2021).

# Relevance:

Over the past few decades, land degradation has contributed significantly to the increased number and size of anthropogenic SDS sources. Current trends in deforestation, agricultural expansion, and more frequent and severe droughts and heatwaves make countries more susceptible to SDS hazards (UNCCD 2021). Exposure to dust can lead to respiratory problems, allergies, and other health issues and the disruption of daily activities and schooling due to poor air quality can also affect children's education and overall wellbeing.

# Data source:

UNCCD’s Sand and Dust Storm susceptibility layer at 1km resolution is used. It employs global datasets for four indicators to estimate the extent of source potential and derive source intensity values: (i) soil texture (proportion of sand, silt, and clay), (ii) soil moisture (absolute minimum value), (iii) soil temperature (absolute maximum value), and (iv) land cover (bare land fraction). (UNCCD, 2024)

# Data processing:

Children’s exposure to sand and dust storms was calculated by simple overlay of the areas where there is SDS susceptibility and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicator:

- Absolute number of children exposed to Sand and Dust Storms
- Relative number of children exposed to Sand and Dust Storms

# Data limitations:

SDS susceptibility layer includes areas of original source but not where the wind could transport the particles. This could underestimate the overall global exposure. The adopted methods in SDS base map also have limited precision in identifying lower intensity sources due to the lack of data as well as the high degree of uncertainty associated with soil-related data (UNCCD, 2024).

# Fires

Wildfires are uncontrolled burns of vegetation, including forests, shrublands, grasslands, savannas, and croplands. They can be caused by human activity or natural causes (UNDRR, 2020). Fires caused deliberately for land clearance (agriculture and ranching) or accidentally (lightning strikes and human error) are a major factor in land-cover variability and change and hence affect fluxes of energy and water to the atmosphere (WMO, 2025).

# Relevance:

## Fires can lead to significant loss of biodiversity, destruction of property, and air pollution but they can also contribute to climate change by releasing large amounts of carbon dioxide and other greenhouse gases into the atmosphere (IPCC, 2022). Climate change is increasing the frequency and intensity of fires.

Higher temperatures, prolonged droughts, and changes in vegetation patterns create conditions that are more conducive to wildfires, and human activities such as land use changes and deforestation also exacerbate the risk of fires (IPCC, 2022). Children are particularly vulnerable as they are exposed to smoke and air pollutants from fires that can lead to respiratory problems, allergies, and other health issues. Fires also impact their overall well-being, education and could cause significant psychological trauma.

# Data source:

Two indicators are used to better understand fires – Frequency and Intensity.

Fire frequency is obtained from NASA’s Fire Information for Resource Management System (FIRMS) is used as a proxy for fire hazard. For CCRI 2025, average fire frequency from 2001-2023 has been considered. The MODIS Fire and Thermal Anomalies product is available from the Terra (MOD14) and Aqua (MYD14) satellites as well as a combined Terra and Aqua (MCD14) satellite product. The sensor resolution is 1 km, and the temporal resolution is daily.

Fire Radiative Power (FRP) is a measure of the energy released by a fire in the form of radiation. It is typically expressed in watts per square meter per steradian per micrometer (W/m²/sr/μm). FRP is an important parameter for understanding the intensity and behavior of fires, as well as their impact on the environment. The historical fires are based on vegetation fires only to capture all climate related events, but it is possible that the data includes human-induced vegetation fires.

# Data processing:

Children’s exposure to fires was calculated by simple overlay of the areas where there is fire frequency above 50 and fire intensity above 10 and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicator:

- Absolute number of children exposed to fire frequency
- Relative number of children exposed to fires frequency
- Absolute number of children exposed to fire intensity
- Relative number of children exposed to fires intensity

# Data limitations:

Fire frequency and intensity are limited in identifying all areas that have potential to experience fires. It is adopted as a proxy for the lack of high-resolution global hazard data for Fire Weather Index (FWI) – a combination of which could give a better picture of fire hazard.

# Air Pollution

Air pollution refers to the presence of substances in the atmosphere that are harmful to human health and the environment. These substances can include particulate matter, nitrogen dioxide, sulfur dioxide, carbon monoxide, and ozone (WHO, 2021).

# Relevance:

## Climate change and air pollution are closely linked. Many activities that produce greenhouse gases also emit air pollutants, which can act as short-lived climate forcers and can warm or cool the Earth's climate over shorter time scales (IPCC, 2022). Air pollution threatens children's health and is the biggest environmental health risk factor (UNICEF, 2024). Exposure to pollutants can lead to respiratory problems.

asthma, and other health issues. Poor air quality can also affect children's development and cognitive function. Air pollution was the second leading risk factor for death among children under five in 2021, after malnutrition.

# Particulate Matter 2.5 (PM2.5):

Fine particle air pollution, or PM2.5, refers to airborne particles measuring less than 2.5 micrometers in diameter that could be emitted from vehicles, residential fuel use, coal-burning power plants, agricultural and industrial activities, waste burning, wildfires, and many other human and natural sources. Among the key air pollutants that are currently measured, long-term exposure to PM2.5 is the most consistent and accurate predictor of poor health outcomes across populations. (Health Effects Institute, 2024)

# Data source:

Data from the Atmospheric Composition Analysis Group (ACAG) were global concentrations of PM2.5 estimated using information from satellite-, simulation- and monitor-based sources was used (Shen et al, 2024). Following the established WHO standards for air quality guidance, a threshold of 5 μg/m3 is adopted (WHO, 2021) and to account for short term variations such as decrease in air pollution during covid-19 pandemic, a ten-year average was considered following expert advice.

# Data processing:

Children’s exposure to particulate matter 2.5 was calculated by simple overlay of the areas where there is observed values of a ten-year average (2012 – 2022) was greater than 5 μg/m3 and the high-resolution gridded global child population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicator:

- Absolute number of children exposed to air pollution
- Relative number of children exposed to air pollution

# Data limitations:

On-the-ground air quality monitoring stations are few and far between in many regions of the world, particularly in low- and middle-income countries which could affect the results and hence the exposure analysis. As noted above, there are several other air pollutants that are not included due to a lack of reliably modelled long-term global data at the time of writing.

# Vector borne diseases

Vector borne disease are human illnesses caused by parasites, viruses, and bacteria that are transmitted by vectors.

# Relevance:

## Climate change can alter the distribution and abundance of vectors, leading to changes in the incidence and geographic range of these diseases. Higher temperatures combined with land use/land cover change are making more areas suitable for the transmission of vector-borne diseases (IPCC, 2022). Children are particularly susceptible to severe health problems from vector-borne diseases. For instance, malaria can cause high fever, anemia, and neurological complications, which are especially dangerous for young children and can also lead to increased mortality (WHO, 2024). Illnesses can also lead to malnutrition, disrupt education and affect a child’s overall well-being.

Note: While there is various vector borne diseases such as dengue, zika and others, due to lack of global data availability, only Malaria was considered in CCRI 2025.

# Malaria

Malaria is a life-threatening disease caused by parasites transmitted to humans through the bites of infected female Anopheles mosquitoes (WHO, 2021). There are 5 Plasmodium parasite species that cause malaria in humans and 2 of these species – P. falciparum and P. vivax – pose the greatest threat. P. falciparum is the deadliest malaria parasite and the most prevalent on the African continent. P. vivax is the dominant malaria parasite in most countries outside of sub-Saharan Africa (WHO, 2021).

# Data source:

Gridded long-term estimates were downloaded from Malaria Atlas Project (MAP, 2025) and estimated from the global malariometric data (Pfeffer et al, 2018)

- Gridded average number of newly diagnosed Plasmodium falciparum cases per 1,000 population from 2012-2022 is used as a proxy for the spread of Malaria by Plasmodium falciparum
- Gridded average number of newly diagnosed Plasmodium vivax cases per 1,000 population from 2012-2022 is used as a proxy for the spread of Malaria by Plasmodium vivax

# Data processing:

All children living in areas with more than 1 case is estimated as children exposed to Malaria (individually calculated for each) and overlaid with high-resolution gridded global children population layer. The results were then summarized to different administrative boundaries as absolute and relative values for all the Member States and territories using zonal statistics.

# Coverage:

Global

# Indicator:

- Absolute number of children exposed to Malaria (Plasmodium Falciparum)
- Relative number of children exposed to Malaria (Plasmodium Falciparum)
- Absolute number of children exposed to Malaria (Plasmodium Vivax)
- Relative number of children exposed to Malaria (Plasmodium Vivax)

# Data limitations:

Due to limitations in data availability, CCRI 2025 indicator only includes estimates based on reported cases and does not include areas susceptible to Malaria based on climate indicators. It is highly recommended to use a combination of both long-term cases and susceptibility.

# Pillar 2 – Child Vulnerability

Children face unique vulnerabilities that make them particularly susceptible to climate and climate-sensitive hazards. Given their unique metabolism, physiology, and developmental needs, children are more vulnerable to extreme events and societal changes than adults. Additionally, children are less able to protect themselves from harm and are more dependent on adults for their safety and care. Addressing these vulnerabilities is crucial for creating resilient and supportive environments that promote children's growth and development.

# CCRI 2025 includes 7 child-specific vulnerability components with 17 indicators:

# Components of Child Vulnerability:

1. Health

---

# 2. Nutrition

# 3. WASH

# 4. Education

# 5. Protection

# 6. Poverty

# 7. Child Survival

# Child Vulnerability

Considerations for vulnerability indicators:

Child vulnerability indicators were chosen after extensive internal consultations with sector-specific and data experts. While there are over 50 child vulnerability indicators, for the purpose of CCRI 2025, 17 are considered across seven components.

All vulnerability indicators are considered at country level and the last available data has been assumed to be current.

All definitions and data on child vulnerability are obtained from data.unicef.org.

Each indicator that is added increases complexity and reduces coverage. Efforts have been made to conduct extensive sensitivity analysis to best combine individual indicators and components.

When a particular indicator is not available for a country, it is not considered in the average. It is possible that a certain amount of bias is introduced in the overall score for countries with minimum number of total indicators.

A combination of indicators showing vulnerability and where data unavailable, proxies using lack of coping capacity is used.

# Health

Three sub-components are considered under health: child health, maternal health and access to electricity with four indicators.

# Child health:

---

Immunization is one of the most cost-effective public health interventions. The first dose of the diphtheria-tetanus-pertussis-containing vaccine (DTP1) serves as a proxy for access to immunization services, while coverage of the third dose (DTP3) is often used as an indicator of how effectively countries are delivering routine immunization services to children (a good proxy for child health). Access to life-saving vaccines to combat diseases is not universal and varies across regions and countries (source).

# Indicators:

- Percentage of surviving infants who received the first dose of DTP-containing vaccine
- Percentage of surviving infants who received the third dose of DTP-containing vaccine

Coverage: Data is available for 195 countries and territories.

Source: WHO/UNICEF estimates of national immunization coverage (WUENIC), 2023 revision

# Data Limitations:

WUENIC is informed by reported administrative data and household surveys, both of which can have limitations including incomplete reporting, misclassification or biases. When data gaps, inconsistencies without explanation or unreliable data exist, WUENIC uses various statistical methods such as interpolation or extrapolation, which may not accurately reflect the reality on the ground. The most recent year estimates are informed by less data as surveys for the youngest cohorts are not available.

# Maternal health:

Despite recent progress, millions of births still occur without any assistance from a skilled attendant each year which is a good proxy for maternal health in a country.

# Indicator:

Percentage of deliveries attended by skilled health personnel

Coverage: Data is available for 192 countries and territories.

Source: Joint UNICEF-WHO Database on Skilled Birth Attendance 2024.

# Data Limitations:

This indicator measures the extent to which the health system can support mothers during childbirth; however, it alone doesn’t show whether delivery care is actually available or accessible when needed and the quality of delivery care being provided. Another limitation is related to the standardization of the ‘skilled’ health personnel across all countries and regions as different countries use different job titles for healthcare workers. In some areas, duties are shifted from trained professionals to less experienced staff which can affect the accuracy of the data collected.

# Health system performance:

Electrification is a proxy of health system performance, that strongly correlates to a variety of other covariates, and access to basic utilities like electricity can enhance the operation of healthcare facilities and services, impacting outcomes like ANC4 and skilled attendance at births.

# Indicator:

Percentage of population with access to electricity

Coverage: Data is available for 212 countries and territories.

Source: World Bank

# Data Limitations:

## The indicator only measures whether people have access to electricity or not which is usually defined as the ability to connect to the official grid provided by the industry. It does not consider quality (voltage fluctuations), reliability (blackouts) or duration (number of hours per day electricity is

# Nutrition

Two indicators are considered under Nutrition: Stunting and Child food poverty.

Stunting is the result of chronic or recurrent undernutrition in-utero and early childhood. Children suffering from stunting may never reach their full possible height nor their full cognitive potential. Stunted children not only earn less as adults as a result of less schooling and learning difficulties when in school, but they are also more likely to be at risk of overweight and obesity than children of normal height (Source).

# Indicator: Prevalence of stunting

(height for age &lt;-2 standard deviation from the median of the World Health Organization (WHO) Child Growth Standards) among children under 5 years of age.

Coverage: Data is available for 163 countries and territories.

Source: UNICEF/WHO/World Bank Joint Child Malnutrition Estimates Expanded Database: Stunting (Survey Estimates) 2023.

Data Limitations: Survey estimates have uncertainty due to both sampling error and non-sampling error (e.g., measurement technical error, recording error, etc.). The JME modelled estimates for stunting take into account estimates of sampling error around survey estimates. While non-sampling error cannot be accounted for or reviewed in full, when available, a data quality review of weight, height and age data from household surveys supports compilation of a time series that is comparable across countries over time.

# Child food poverty

Child food poverty is a distinct metric that refers to a child’s inability to access and consume a nutritious and diverse diet in early childhood. It is measured using the UNICEF and WHO dietary diversity scores. Children are defined as living in severe child food poverty if they consume foods from two or fewer food groups out of eight food groups (Source).

# Indicator: Percentage of children 6–23 months of age

consuming foods and beverages from zero, one or two out of eight defined food groups1 during the previous day (severe child food poverty).

Coverage: Data is available for 108 countries and territories.

Source: UNICEF Global Database on Infant and Young Child Feeding. Child food poverty, December 2023.

Data Limitations: As household surveys are the primary source of data on child food poverty, the estimates come with levels of uncertainty due to both sampling and non-sampling error (e.g. misclassification of food items in food groups, recording error etc.).

# WASH

Securing access to safe drinking water, sanitation and hygiene reduces illness and death, especially among children and it is critical for their survival and growth. Three indicators are considered under WASH.

# Water

## At least basic drinking water refers to water from an improved source, provided collection time is not more than 30 minutes for a round trip, including queuing (source) where the improved sources must be accessible on premises, available when needed and free from contamination.

# Indicator: Proportion of population using improved drinking water sources no more than 30 mins roundtrip

Coverage: Data is available for 207 countries and territories

Source: WHO/UNICEF Joint Monitoring Programme – WASH in households 2023 update.

# Sanitation

At least basic sanitation refers to use of improved facilities that are not shared with other households (source) and has a ‘safely managed’ service, excreta must either be safely disposed of in situ or removed and treated offsite.

# Indicator: Proportion of population using improved sanitation facilities not shared with other households

Coverage: Data is available for 206 countries and territories.

Source: WHO/UNICEF Joint Monitoring Programme – WASH in households 2023 update.

# Hygiene

Basic hygiene refers to availability of a handwashing facility with soap and water at home (source).

# Indicator: Proportion of population with a handwashing facility with soap and water available at home

Coverage: Data is available for 84 countries and territories.

Source: WHO/UNICEF Joint Monitoring Programme – WASH in households 2023 update.

# Data Limitations for WASH

JMP produces internationally comparable estimates based on national data sources. Estimates are modelled using all available data points and at-least basic is preferred over safely managed (SDG indicators) due to data availability.

# Education

The education and training that children receive in secondary school equip them with skills that are necessary to fully participate in society. Though the duration in each country vary, secondary education typically covers ages 12 to 17 and is divided into two levels: lower secondary education (spanning 3 to 4 years) and upper secondary education (spanning 2 to 3 years). Although notable progress has been made in the past few decades, challenges remain in reducing regional disparities and inequalities among secondary school-age students from different socioeconomic backgrounds. (source).

There indicators are considered under education: Lower secondary out of school rate, lower secondary completion rate and learning poverty.

# Lower secondary out of school

# Indicator: Percentage of children out of school in lower secondary education

Coverage: Data is available for 115 countries and territories.

Source: UNICEF global databases, 2024, based on DHS, MICS and other national surveys.

# Data Limitations

The main limitation lies in the data sources. Administrative records are not well-suited to capture out-of-school populations, as they only include children who are registered within the education system. The recommended approach is to estimate out-of-school rates using household survey data. However, such surveys are not always conducted regularly or widely—particularly in countries or regions with high rates of children not attending school.

# Lower secondary completion rate

---

# Percentage of cohort of children or young people three to five years older than the intended age for the last grade of lower secondary education who have completed that level of education.

Indicator: Completion rate of children in lower secondary education

Coverage: Data is available for 112 countries and territories.

Source: UNICEF global databases, 2024, based on DHS, MICS and other national surveys.

Data Limitations: A key limitation of this indicator is that it measures school completion 3–5 years after the expected age of graduation. As a result, it can only be calculated when at least three years have passed since a child was expected to complete a given level of education.

# Learning poverty

The learning poverty indicator was launched by the World Bank and the UNESCO Institute for Statistics in 2019 helps to better understand the global learning crisis. High rates of learning poverty are an early signal that education systems are failing to ensure that children develop critical foundational skills (source).

Indicator: Rate of learning poverty

Coverage: Data is available for 122 countries and territories.

Source: UNICEF global databases, 2024, based on DHS, MICS and other national surveys.

Data Limitations: While this indicator effectively combines two critical aspects of education—school access and learning outcomes—it is significantly limited by the availability and coverage of data on learning outcomes. In many cases, these data are either outdated, infrequent, or not representative, which restricts the robustness of the measure.

# Protection

Two indicators are considered under Child Protection: Child labor and Child marriage

# Child labor

Children around the world are routinely engaged in paid and unpaid forms of work that are not harmful to them. However, they are classified as child labourers when they are either too young to work or are involved in hazardous activities that may compromise their physical, mental, social or educational development. A child is considered to be involved in child labour under the following conditions:

- (a) children 5–11 years old who, during the reference week, did at least one hour of economic activity and/or more than 21 hours of unpaid household services,
- (b) children 12–14 years old who, during the reference week, did at least 14 hours of economic activity and/or more than 21 hours of unpaid household services,
- (c) children 15–17 years old who, during the reference week, did at least 43 hours of economic activity.

Indicator: Percentage of children 5–17 years old involved in child labour

Coverage: Data is available for 85 countries and territories.

Source: UNICEF global databases, 2024, based on DHS, MICS and other national surveys.

## Data Limitations: While the concept of child labour includes working in activities that are hazardous in nature, to ensure comparability of estimates over time and to minimize data quality issues, work beyond age-specific hourly thresholds is used as a proxy for hazardous work. Further methodological work is needed to validate questions specifically aimed at identifying children in hazardous working conditions. Similarly, the worst forms of child labour are not currently captured in regular household surveys given difficulties in accurately and reliably measuring them.

# Child Marriage

Marriage before the age of 18 is a fundamental violation of human rights. Many factors interact to place a child at risk of marriage, including poverty, the perception that marriage will provide ‘protection’, family honor, social norms, customary or religious laws that condone the practice, an inadequate legislative framework and the state of a country’s civil registration system. While the practice is more common among girls than boys, it is a violation of rights regardless of sex (source).

# Indicator

Total number of girls and women of all ages who were first married or in union before age 18

# Coverage

Data is available for 140 countries and territories.

# Source

UNICEF global databases, 2024, based on DHS, MICS and other national surveys.

# Data Limitations

The measure of child marriage is retrospective in nature by design, capturing age at first marriage among a population that has completed the risk period (i.e., adult women). Thus there is an inherent time lag between the moment at which child marriages occur and when they show up in the data: Prevalence estimates reflect child marriages that occurred at least two years and as many as six or more years prior to the reported year. While it is also possible to measure the current marital status of girls under age 18, such measures would provide an underestimate of the level of child marriage, as girls who are not currently married may still do so before they turn 18 (UNICEF, 2020).

# Poverty

# Multi-dimensional poverty

Child poverty measures the means (or the lack thereof) to realize child rights that crucially and directly rely on continuously/periodically using material elements such as goods and services. These rights include clothing, education, health, housing, information, nutrition, play, sanitation, and water. The lack of these basic needs often results in deficits that cannot easily be overcome later in life. Even when not clearly deprived, having poorer opportunities than their peers in any of the above can limit future opportunities (source).

# Indicator

Percentage of children with severe material deprivation

# Coverage

Data is available for 72 countries and territories.

# Source

UNICEF global databases

# Data Limitations

To ensure international comparability and to be able to aggregate across countries, the indicators and thresholds used to establish severe deprivation do not necessarily coincide with more nuanced and appropriate measure at the national level.

# Under five covered by social protection

Social protection is a set of measures that allows all members of society to access essential health care, and provides them with income security. Child-sensitive social protection systems – programmes such as cash transfers, health insurance and education subsidies – can help make sure that no child is left behind because of poverty. But globally, few children benefit. For almost three out of every four children, social protection programmes remain out of reach (source).

# Indicator

Percentage of children under 5 covered by social protection

# Coverage

## Data is available for 182 countries and territories.

# Child Survival

# Under five mortality

The under-five mortality rate refers to the probability a newborn would die before reaching exactly 5 years of age, expressed per 1,000 live births (source).

Indicator: Mortality rate under five per 1000 live births

Coverage: Data is available for 199 countries and territories.

Source: UN Inter-agency Group for Child Mortality Estimation

Data Limitations: &lt;&gt;

# Section 2: Methodology

CCRI composite index is designed to encompass a comprehensive list of children’s exposure to various hazards and vulnerabilities. Each pillar is processed separately with an internally established semi-automated data pipeline and follows multiple steps.

# Data collection and cleaning

For pillar 1 hazard data, raw raster data collected from various established data sources is processed using Google Earth Engine. Raster data is first uploaded as an Image Collection asset representing each hazard. Image Collections are processed into a single layer by spatially assembling into a continuous image using mosaicking. All raster tiles are merged and clipped to represent global land boundaries using coastline layer and as discussed earlier 100-year return period is used for probabilistic models and the most recent ten-year average of long-term observations.

For pillar 2, all indicators are downloaded using UNICEF’s Data Warehouse – SDMX API.

# Thresholding

For pillar 1 hazard data, thresholds are chosen based on existing literature and expert feedback. Meticulous steps were taken to widely consult with the external experts and review the most recent state of the art research available. It is important to note that by choosing global thresholds, it is possible to over- or under- estimate the exposure of children to individual hazards.

| Hazard                 | Threshold                                                     | Notes                     |
| ---------------------- | ------------------------------------------------------------- | ------------------------- |
| Riverine Flood         | &gt;1 cm depth                                                |                           |
| Coastal Flood          | All                                                           | Binary layer used         |
| Tropical Storm         | &gt;63 km/hr                                                  |                           |
| Agricultural Drought   | &gt;30% cropland affected                                     |                           |
| Meteorological Drought | &lt;-1 SPI values                                             |                           |
| Fire                   | &gt;Mean (frequency, intensity)                               |                           |
| Heatwave               | &gt;Mean (frequency, duration, severity, extreme temperature) |                           |
| Sand and dust storm    | All                                                           | Susceptibility layer used |
| Air pollution          | &gt;5 AQG                                                     |                           |
| Malaria                | &gt;1 case per 1000 population                                |                           |

---

# Overlay and Summarizing

For pillar 1 hazard data, using Worldpop’s gridded child population layer, both the absolute (total number of children) and relative (percentage of children) exposure of children are calculated for every hazard using a simple overlay technique. Zonal statistics is used to summarize the total and percentage children exposed by countries and territories.

# Imputation of Missing Values

Missing values are dealt based on complete case analysis or case deletion where missing records are completely omitted from the analysis. This approach ignores possible systematic differences between complete and incomplete samples and could lead to biased estimates. No imputation was used to fill missing data unless it has already been imputed in the modelled data sources for a few vulnerability variables.

# Normalization

Normalization is a statistical technique to adjust data from different sources to a common scale without distorting differences in the ranges of values. This ensures that all variables contribute equally to the final index. Common methods include min-max normalization, where data is scaled to a range of 0 to 1, and z-score normalization, which adjusts data based on the mean and standard deviation.

In CCRI 2025, the values are normalized using the min-max technique to a 0-10 scale for all indicators, components and pillars. Min-Max normalizes indicators to an identical range by subtracting the minimum value and dividing by the range of the indicator values, noting that extreme values/or outliers could distort the transformed indicator. But one notable advantage is that it could widen the range of indicators lying within a small interval, increasing the effect on the composite indicator.

The min and max values are considered where skewness is lower than 2 AND kurtosis is lower than 3.5. Skewness and kurtosis are calculated iteratively for the whole dataset without the obvious outliers, until pre-set conditions are met. The minimum and maximum data point of the remaining dataset are taken as min and max.

Normalized indicator score (0-10): 10 - (baseline maximum – raw data value) / (baseline maximum – baseline minimum) x 10

Include distribution for each indicator in the annex

| Indicator                                      | Min | Max | Notes                                                                                |
| ---------------------------------------------- | --- | --- | ------------------------------------------------------------------------------------ |
| Children exposed to riverine floods (absolute) | 2   | 8   | Areas with no data or with less than 100 people exposed are considered 0.1           |
| Children exposed to riverine floods (relative) | 1   | 70  | Areas with no data or with less than 0.05% of population are assigned a score of 0.1 |
| Children exposed to coastal floods (absolute)  | 2   | 7   | Log transformation applied for all values above 0                                    |
| Children exposed to coastal floods (relative)  | 1   | 20  |                                                                                      |
| Children exposed to pluvial floods (absolute)  | 2   | 8   |                                                                                      |
| Children exposed to pluvial floods (relative)  | 10  | 100 |                                                                                      |

---

# Children exposed to tropical storm

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 10  | 100 |                                                   |

# Children exposed to agricultural drought

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 10  | 90  |                                                   |

# Children exposed to meteorological drought - spi

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 10  | 100 |                                                   |

# Children exposed to meteorological drought – sma

| Type     | Min | Max | Notes |
| -------- | --- | --- | ----- |
| Absolute | 3   | 8   |       |
| Relative | 10  | 100 |       |

# Children exposed to fire intensity

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 7   | Log transformation applied for all values above 0 |
| Relative | 10  | 60  |                                                   |

# Children exposed to fire frequency

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 7   | Log transformation applied for all values above 0 |
| Relative | 10  | 80  |                                                   |

# Children exposed to heatwave frequency

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 10  | 100 |                                                   |

# Children exposed to heatwave duration

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 10  | 100 |                                                   |

# Children exposed to heatwave severity

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 10  | 100 |                                                   |

# Children exposed to extreme temperature

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 10  | 100 |                                                   |

# Children exposed to sand and dust storm

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 7   | Log transformation applied for all values above 0 |
| Relative | 1   | 100 |                                                   |

# Children exposed to air pollution (PM2.5)

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 1   | 100 |                                                   |

# Children exposed to Malaria P. Falciparum

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 1   | 100 |                                                   |

# Children exposed to Malaria P. Vivax

| Type     | Min | Max | Notes                                             |
| -------- | --- | --- | ------------------------------------------------- |
| Absolute | 2   | 8   | Log transformation applied for all values above 0 |
| Relative | 1   | 100 |                                                   |

# Vulnerability

| Min | Max | Notes |
| --- | --- | ----- |
|     |     | 25    |

---

# Health

| DTP1 access            | 45  | 98  | Values reversed in normalization |
| ---------------------- | --- | --- | -------------------------------- |
| DTP3 access            | 40  | 98  | Values reversed in normalization |
| Skilled birth coverage | 25  | 100 | Values reversed in normalization |
| Access to electricity  | 10  | 100 | Values reversed in normalization |

# Nutrition

| Stunting           | 1   | 50  |
| ------------------ | --- | --- |
| Child Food Poverty | 0   | 70  |

# WASH

| At-least basic drinking water | 35  | 100 | Values reversed in normalization |
| ----------------------------- | --- | --- | -------------------------------- |
| At-least basic sanitation     | 10  | 100 | Values reversed in normalization |
| Basic hygiene                 | 4   | 100 | Values reversed in normalization |

# Education

| Lower secondary out of school   | 1   | 70  | Values reversed in normalization |
| ------------------------------- | --- | --- | -------------------------------- |
| Lower secondary completion rate | 1   | 100 | Values reversed in normalization |
| Learning poverty                | 3   | 98  |                                  |

# Protection

| Child labor    | 1   | 40  |
| -------------- | --- | --- |
| Child marriage | 0   | 76  |

# Poverty

| Child poverty                           | 3   | 83  |                                  |
| --------------------------------------- | --- | --- | -------------------------------- |
| Under five covered by social protection | 0   | 100 | Values reversed in normalization |

# Survival

Under five mortality
1
30

To ensure similar trend in normalization for all indicators, where higher values show worse conditions, 10 of the vulnerability indicators have been reversed as highlighted in the table below.

# Aggregation

Aggregation involves combining multiple indicators or data points into a single composite score. This step typically uses weighted averages or other statistical methods to summarize the data. Aggregation helps in simplifying complex data sets into a more understandable and actionable format.

CCRI 2025 uses a blended aggregation method using both geometric and arithmetic average. Geometric mean is used to aggregate at pillar level, as well as to aggregate relative and absolute exposure to individual hazard components in Pillar 1. Arithmetic mean is used where we have two indicators that show compensability and used to aggregate the indicators and components in Pillar 2. By adopting a blended method, CCRI can capture both the compounding effects of hazards as well as the independent effects of each vulnerability indicator.

## Any future improvements in any of the indicators will directly influence the index. If there are no values for a specific indicator, it is not counted towards the aggregation. For pillar 1 hazard layers, all pixels with no values are assumed to be no hazard.

# Correlation

# Include correlation matrix

# Sensitive Analysis

# Composite Index

Index generation is the final step where normalized and aggregated data are combined to produce a comprehensive risk index. This involves calculating a composite score that represents the overall climate risk for children. The index can be used to compare different regions or populations, identify high-risk areas, and inform policy decisions. The process includes validating the index through statistical analysis and expert review to ensure its accuracy and reliability.

CCRI composite index also uses a 0-10 scale, where 10 represents the highest multi-hazard risk.

| 1. Raw raster data obtained                                   | 2. 100-year return period                                                         | 3. Individual thresholding                                                                                              | 4. Absolute and relative exposure of children                                             |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| for each hazard indicator                                     | chosen for probabilistic model and the most recent ten-year average               | applied to each layer based on recent literature and expert consultations (>1 cm of flood, >68 km/hr for cyclones, etc) | calculated for each hazard                                                                |
| 5. Log transformation                                         | 6. Skewness and kurtosis                                                          | 7. Min-Max Normalization                                                                                                | 8. Geometric average used to aggregate individual absolute and relative hazard indicators |
| applied for absolute exposure                                 | assessed and iteratively outliers removed for both absolute and relative exposure | applied for each indicator                                                                                              |                                                                                           |
| 9. Geometric average used                                     | 10. Pillar 1 generated on a 0-10 scale                                            |                                                                                                                         |                                                                                           |
| Raw data obtained for each vulnerability indicator            | 2. Only the most recent available data considered                                 | 3. Skewness and kurtosis assessed and iteratively outliers removed                                                      | 4. Min-Max Normalization applied for each indicator                                       |
| 5. Arithmetic average used to aggregate individual indicators | 6. Arithmetic average used to aggregate individual components                     | 7. Pillar 2 aggregate generated on a 0-10 scale                                                                         |                                                                                           |

# Limitations

## 27

# Composite indicators are valuable tools for summarizing complex, multidimensional issues into a single, easily understandable figure. However, they are not without their limitations.

- Combining multiple indicators into one can obscure the individual performance and trends of the underlying components. This lack of transparency can make it difficult to understand what is driving the overall score and to identify specific areas needing improvement.
- A low CCRI score might hide poor performance in specific sub-areas, as strong performance in other areas can compensate for weaknesses. This can lead to misleading policy conclusions if not accompanied by analysis of the individual indicators.
- The single CCRI number can invite overly simplistic interpretations and policy responses, neglecting the nuances and complexities of the underlying dimensions.
- Different indicator and threshold selections could lead to different conclusions. While every measure was taken to consult and choose the indicators carefully, it is important for the users to apply caution in directly using the values for decisions.
- Missing values of vulnerability indicators could affect the overall score.
- Choice of normalization, aggregation and weighting can affect the overall score.

Cautious interpretation of results and triangulating with other indicators and field level evidence are highly recommended, to ensure CCRI’s effective use in policymaking and analysis.

# Pixel-level multi-hazard Children Climate Risk Index

This section outlines the process of calculating the Children Climate Risk Index at the pixel level, using a multi-step methodology that integrates various climate risk factors. The index aims to assess the exposure of child populations to climate and climate-sensitive hazards. Pixel-level analysis is performed to capture fine-grained variations in climate risks within a country, enabling the identification hotspots that national averages may overlook. This approach allows for a more precise understanding of climate risks at both local and national levels, with the flexibility to aggregate data to administrative levels 0, 1, or 2 based on the specific use case.

# Data Processing:

1. Data preparation
1. Loading and Masking – Reads geospatial images and keeps only land pixels.
1. Cleaning – Removes NaNs, zeros, and negative values.
1. Resampling - Resamples the data to a consistent 10 km resolution using the maximum resampling method to preserve the highest values.
1. Transforming – Applies log transformation and z-score based scaling for normalization.
1. Standardized Precipitation Index and Soil Moisture Anomaly data are already z-score based scaled.
1. Trimming Outliers – Iteratively removes extreme values to improve data distribution.
1. Analyzing & Visualizing – Checks skewness, kurtosis, and normality, then plots histograms.
1. All data layers are stacked into a multi-layer array.

---

# Histogram and KDE for heatwave_frequency_resampled tif after Log Transformation and MinMax Scaling

600005000040000[₃₀₀₀₀2000010000
Scaled Data

# Histogram of heatwave frequency after log transformation and z-score scaling

# 2. Principal Component Analysis (PCA):

PCA is applied to reduce the dimensionality of the climate risk data while preserving as much variability as possible. This allows us to identify the most significant components that explain the variance in the dataset and provides ways to use the weights for each PCs for indicator construction based on it.

1. From the multi-layer array Principal Components are identified
2. The dimensionality is reduced to 11 (11 principal components)

Given a standardized dataset

𝑋 (shape: 𝑚×𝑛, where 𝑚 is the number of land pixels and 𝑛 is the number of features):

𝑍=𝑋𝑊

where:

- 𝑋 is the standardized data matrix (𝑚×𝑛)
- 𝑊 is the PCA loadings matrix (𝑛×𝑝), where 𝑝 is the number of selected principal components
- 𝑍 is the transformed data matrix in the PCA space (𝑚×𝑝)

c. Explained variance by PCA components: 91.06%

## 29

# PCA Loadings (Hazard Layers vs Principal Components)

| ASI_cropland                               | 0.077 | 0.03   | -0.2   | -0.12   | 0.21    | 0.32   | 0.86   | -0.061 | 0.09    | -0.071  | -0.14  |     |
| ------------------------------------------ | ----- | ------ | ------ | ------- | ------- | ------ | ------ | ------ | ------- | ------- | ------ | --- |
| coastal_flood_mosaictif 00031              | 0.019 | -0.067 | -0.28  | 0.49    | ~0.56   | 0.042  | -0.43  | -0.37  | 0.17    | 064     |        |     |
| ERAS_IOOyr_RP                              | 0.32  | 0.33   | -0.15  | 0.028   | -0.053  | -0.092 | 0.05   | 0.099  | 0.11    | 0.24    | -0.12  |     |
| extreme_heat_days                          | 0.29  | 0.41   | -0.11  | 0.025   | 0.093   | -0.12  | 0.053  | 0.097  | 0.09    | 0.24    | 0.082  |     |
| FIRMS\_ MODIS Mean Annual Count            | 0.25  | -0.31  | -0.39  | -0.07   | -0.26   | -0.13  | -0.084 | 0.027  | 0.018   | 0.0084  | 0.017  |     |
| FIRMS\_ MODIS MeanAnnual FRP 2001 2023.tif | 0.28  | 0.29   | -0.38  | -0.12   | -0.21   | -0.08  | -0.082 | 0.055  | 0.026   | -0.0031 | -0.017 | 0.4 |
| heatwave_duration                          | 0.38  | -0.16  | 0.31   | -0.028  | -0.018  | 0.044  | 0.0035 | -0.11  | -0.039  | -0.085  | -0.084 |     |
| heatwave_frequency                         | 0.38  | -0.16  | 0.3    | -0.018  | -0.0085 | 0.044  | 0.0082 | -0.11  | -0.034  | -0.096  | -0.077 |     |
| heatwave_severity                          | 0.32  | -0.23  | 0.41   | -0.1    | -0.058  | 0.04   | 0.015  | -0.09  | -0.053  | -0.072  | -0.088 | 0.2 |
| JBA_FLSW                                   | 0.096 | -0.3   | 0.14   | 0.22    | 0.31    | 0.11   | 0.014  | 0.079  | 0.24    | 0.69    | 0.42   |     |
| Pf_average                                 | 0.13  | -0.016 | -0.34  | 0.47    | -0.082  | -0.13  | 0.079  | -0.28  | -0.13   | -0.034  | 0.17   |     |
| Pv_average                                 | 0.073 | 0.0035 | -0.072 | 0.59    | 0.41    | 0.1    | -0.24  | -0.12  | 0.17    | -0.17   | ~0.48  |     |
| pm25                                       | 0.38  | 0.11   | 0.001  | 0.077   | 0.016   | 0.033  | 0.045  | 0.066  | 0.00091 | -0.081  | 0.095  |     |
| river_flood_mosaic.tif                     | 0.14  | -0.11  | -0.022 | 0.065   | 0.37    | -0.26  | 0.067  | 0.79   | -0.22   | -0.23   | 0.035  | 0.2 |
| sand_dust_storm                            | 0.15  | 0.5    | 0.24   | -0.025  | -0.082  | -0.13  | 0.024  | 0.069  | 0.0044  | 0.12    | -0.019 |     |
| storm_mosaic tif                           | 0.096 | 0.04   | -0.18  | 0.46    | 0.33    | 0.019  | -0.27  | 0.043  | 0.63    | -0.14   | -0.027 | 0.4 |
| SPI                                        | 0.19  | 0.26   | 0.083  | 1.5e-05 | 0.22    | 0.26   | -0.12  | -0.14  | -0.13   | -0.39   | 0.66   |     |
| SMA                                        | 0.11  | 0.068  | -0.21  | -0.21   | 0.14    | 0.59   | -0.29  | 0.071  | ~0.52   | 0.29    | -0.22  |     |

# Principal Components

Heatmap showing the relationship between hazard layers and principal components.

A weighted combination of the PC loadings and explained variance is computed to create a single risk indicator with range of 0 to 10.

The weighted contribution of each feature is calculated using the explained variance of each principal component:

Wweighted = ∑i=1k viWi

Where vi is the explained variance ratio of the ith principal component, Wi is the loading vector for the ith PC, k is the number of selected PCs (e.g., 8 in this case), and Wweighted is the final weighted combination of loadings (n-dimensional vector).

The final composite indicator for each land pixel is obtained by applying the weighted loadings:

I = XWweighted

where I is the raw indicator score for each land pixel.

To bring the values into a range of 0 to 10, Min-Max scaling is applied:

Inormalized = 10 × (I - min(I)) / (max(I) - min(I))

## A new raster is created, where the risk indicator values are assigned to valid land pixels. The final composite indicator provides a single risk score for each land pixel, representing the overall climate risk exposure in that area.

# 3. Combine with Pillar 2 data

The geometric mean is used to combine the Pillar 1 and Pillar 2 indicators, as it accounts for their multiplicative relationship and ensures that both pillars contribute proportionally to the overall risk score.

0 - 0.130.13 - 0.250.25 - 0.460.46 - 1.061.06 - 1.471.47 - 1.981.98 - 2.642.64 - 3.673.67 - 5.035.03 - 7.17

# Averaged Pillar 2 indicators at country level

## Pillar 2 indicators are country-level indicators, with the assumption that Pillar 2 indicators are homogeneous across each country. Pixel-level Pillar 1 data is averaged with the country-level Pillar 2 indicator.

# 4. Child Population Exposure estimation

The thresholds are applied to categorize child populations based on different levels of climate risk exposure. The child population exposure is calculated at various risk thresholds, such as the mean and percentiles, to estimate the number of children affected at different risk levels.

| Threshold                    | Value | Child Population Exposure to Risk |
| ---------------------------- | ----- | --------------------------------- |
| Mean of risk_sum_normalized  | 2.54  | 1,787,430,778                     |
| Mean + 1 Standard Deviation  | 3.96  | 1,224,995,637                     |
| Mean + 2 Standard Deviations | 5.38  | 441,939,000                       |
| 75th Percentile              | 3.38  | 1,514,398,100                     |
| 90th Percentile              | 4.79  | 892,295,847                       |
| 95th Percentile              | 5.68  | 272,122,093                       |
| 99th Percentile              | 6.63  | 18,895,648                        |

## Child population exposure based on different threshold values

# Child Population exposure with 75 percentile Threshold

| Canada    | Hudson Bay  | Labrador Sea        | United Kingdom | Denmark        | Ireland      | Germany            | Poland      | Belarus      |
| --------- | ----------- | ------------------- | -------------- | -------------- | ------------ | ------------------ | ----------- | ------------ |
| France    | Austria     | Ukraine             | Kazakhstan     | Mongolia       | Romania      | United States      | Spain       | Italy        |
| Greece    | Turkiye     | Turkmenistan        | Kyrgyzstan     | North Atlantic | Portugal     | Syria              | China       | South Korea  |
| Japan     | Mexico      | Western Sahara      | Algeria        | Libya          | Egypt        | Cuba               | Puerto Rico | Saudi Arabia |
| Oman      | Philippines | Guatemala           | Nicaragua      | Venezuela      | Nigeria      | Ethiopia           | Vietnam     | Guyana       |
| Colombia  | Suriname    | Ecuador             | Peru           | Brazil         | Bolivia      | Namibia            | Zimbabwe    | Malaysia     |
| Indonesia | Coral Sea   | South Pacific Ocean | Uruguay        | Argentina      | South Africa | Great Barrier Reef |             |              |

# Child Population exposure with 90 percentile Threshold

# 5. Discussion

Sensitivity analysis can be conducted to evaluate the impact of different resampling methods, aggregation approaches between Pillar 1 (P1) and Pillar 2 (P2) data, varying numbers of principal components (PCs) for Pillar 1 data, and diverse normalization methods.

By applying these methods to the Pillar 1 values at the pixel level, hazard profiles can be generated for various administrative boundary levels, such as admin level 3. These profiles will provide insights into which types of hazards are dominant within specific regions, such as an admin level 3 boundary, allowing for a more localized understanding of climate risks.

## Additionally, these hazard profiles can be identified at the pixel level, providing even more granular and precise data that can help target interventions, policy making, and resource allocation at a detailed spatial level. This approach ensures that assessments and actions can be tailored to the specific climate risks faced by different areas, contributing to more effective and context-aware decision-making.

# Assumptions / Limitations

# Advantages

# Section 4: Results and Interpretation

# Overall Analysis

# Future work

# Limitations:

- The composite index must not be mistaken for a comprehensive climate vulnerability scoring.
- The index focuses on extreme weather events such as storms, floods and heatwaves but does not consider slow-onset processes such as rising sea levels, glacier melting or ocean warming and acidification.
- More specifically, not too far-reaching conclusions should be drawn for the purpose of political discussions regarding which country or region is the most vulnerable to climate change.
- Also, it is important to note that the occurrence of a single extreme event cannot be easily attributed to anthropogenic climate change. It is important to invest more in attribution science to better understand and estimate the impact of climate change.
- A combination of probabilistic models and past data and should not be used as a basis for a linear projection of future climate impacts.

# External Data Advisors

# Systematic Review

# Reproducibility Package

&lt; include CCRI Reproducibility Package&gt;

# Programming Environment

# Include Data Map

# Data Linkage table (could be the same as catalog)

# Master Dataset

# Data Flow chart

# Disclaimers

- Include map disclaimers
- CCRI doesn’t quantify the impact to climate change
- CCRI only looks at how many children are already vulnerably who are also exposed to climate-related hazards
- Worldpop data limitations apply to population estimates and are all 2024 estimates
- Some hazards are probabilistic and some are observation-based
- Notes on hazards that are relevant but without global open data

---

There are dimensions of vulnerability that although very important are hard to measure consistently across countries so are difficult to include in a global measure. Include a note on the Number of countries with survey data and dimensions of vulnerability - acknowledging data gaps and how missing data is dealt with and sub-national limitations. Add any limitations on Worldpop data – pop movement not accounted for. The data presented are global estimates based on a range of publicly available datasets and do not necessarily represent datasets submitted to UN agencies by national governments. All indices are a relative comparison between countries included in the model, meaning that the performance of a country on the different indices is better or worse in comparison to all other countries included in the model.

# Data licensing and copyrights

All data used in CCRI 2025 are open source.

# Appendix

# Data catalog

| Hazards         | Type                             | Data type     | Indicator(s)                                    | Description                         | Resolution            | Overall Thresholds        |             |
| --------------- | -------------------------------- | ------------- | ----------------------------------------------- | ----------------------------------- | --------------------- | ------------------------- | ----------- |
| Floods          | Riverine                         | Probabilistic | 100 year return period                          | Children exposed to riverine floods | Riverine flood hazard | 90m                       | 01 and 0.15 |
| Floods          | Coastal                          | Probabilistic | 100 year return period                          | Children exposed to coastal floods  | Coastal flood hazard  | Om                        | None        |
| Floods          | Pluvial                          | Probabilistic | 100 year return period                          | Children exposed to pluvial floods  | Pluvial flood hazard  | 30m                       |             |
| Tropical Storms | Winds                            | Probabilistic | 100 year return period                          | Children exposed to windspeed       | Wind speed            | 10km                      | 63 km/hr    |
| Droughts        | Agricultural                     | Observed      | Children exposed to agricultural droughts       | Agricultural Stress Index           | 1km                   | &gt;50% cropland affected |             |
| Droughts        | Soil Moisture Anomaly            | Observed      | Children exposed to meteorological droughts     | Ensemble observation                | 10km                  |                           |             |
| Droughts        | Standardized Precipitation Index | Observed      | Children exposed to dry condition on the ground | CHIRPS                              | 5km                   |                           |             |
| Heatwaves       | Heatwave frequency               | Observed      | Children exposed to heatwaves frequency         | ERAS-LAND                           | 10km                  | Mean                      |             |
| Heatwaves       | Heatwave duration                | Observed      | Children exposed to heatwaves duration          | ERAS-LAND                           | 10km                  | Mean                      |             |
| Heatwaves       | Heatwave severity                | Observed      | Children exposed to heatwaves severity          | ERAS-LAND                           | 10km                  | Mean                      |             |

---

# Hazards

| Type          | Data type           | Indicator(s) | Description                                            | Resolution         | Overall Thresholds |
| ------------- | ------------------- | ------------ | ------------------------------------------------------ | ------------------ | ------------------ |
| Heatwaves     | Heatwave frequency  | Observed     | Children exposed to heatwaves frequency                | ERAS-LAND          | 1Okm Mean          |
| Heatwaves     | Heatwave duration   | Observed     | Children exposed to heatwaves duration                 | ERAS-LAND          | 1Okm Mean          |
| Heatwaves     | Heatwave severity   | Observed     | Children exposed to heatwaves severity                 | ERAS-LAND          | Okm Mean           |
| Heatwaves     | Extreme hot days    | Observed     | Children exposed extreme heat days                     | ERAS-LAND          | 1Okm deg           |
| Pollution     | Fire                | Observed     | Children exposed to fires                              |                    | Frequency          |
| Pollution     | Fire                | Observed     | Children exposed to fires                              |                    | Frequency          |
| Pollution     | Sand and Dust Storm | Observed     | Children exposed to sand and dust storm                | SDS Susceptibility | Ikm                |
| Air pollution | PM 25               | Observed     | Children exposed to air pollution                      | PM 25              | 25 AQG             |
| Epidemics     | Malaria             | Modelled     | Children exposed to malaria caused by Plasmodium Vivax | Incidence rate of  | Skm                |

# Abbreviations and Acronyms

NO_CONTENT_HERE

# Key concepts

Climate data refers to measurements of atmospheric conditions over time and encompasses a wide range of meteorological variables – from temperature, precipitation, sea level rise and wind patterns. Climate data is used to better understand long term climate patterns, trends, and future conditions. This could be both observed and/or modelled data and includes both historical data and future projections.

Climate hazards refers to natural events that are predominantly hydro-meteorological in nature such as floods, tropical storms, heatwaves, wildfires and droughts. These hazards can be exacerbated by climate change, leading to increased frequency, intensity, and unpredictability. Understanding climate hazards is core to risk analysis, emergency preparedness and planning for effective mitigation and adaptation.

Climate change refers to the change in climate over extended period caused by natural processes such as volcanic eruptions or variations in solar radiation as well as human activities such as over burning fossil fuels, deforestation and over emission of greenhouse gases. There is adequate evidence that anthropogenic climate change is increasing the frequency and intensity of climate hazards as well as influence along with existing natural variability that causes climate hazards. In other words, not all climate hazards are results of human-induced climate change. Attribution to climate change is a complex process and at the time of this writing, there is still limited data available to differentiate the two.

Probabilistic hazard models: A probabilistic model for any hazard estimates the likelihood and impact of hazardous events by integrating historical data, relevant modeling techniques, probability analysis, and simulations and are available in different return periods.

Return periods:

## NO_CONTENT_HERE

A return period represents the average interval of time between occurrences of the event. It is important to note that this does not mean the event will happen exactly once every 100 years. Instead, it indicates a 1% probability of the event occurring in any given year. Similarly, a 10-year return period event has a 10% probability of occurring in any given year.

A 100-year return period has been chosen for all probabilistic models used in CCRI 2025 as it has a chance of an event of a considerable magnitude happening within a child’s lifetime. For example, a 100-year flood is a flood event that has a 1% probability of being equaled or exceeded in any given year. There is approximately a 63.4% chance of experiencing at least one 100-year flood within a 100-year period.

| Return Period (years) | Probability of experiencing at least one event in a lifetime |
| --------------------- | ------------------------------------------------------------ |
| 2                     | 100%                                                         |
| 5                     | 100%                                                         |
| 20                    | 99.41%                                                       |
| 50                    | 86.74%                                                       |
| 100                   | 63.40%                                                       |
| 500                   | 18.14%                                                       |
| 1000                  | 9.52%                                                        |

# Aggregation methods:

The arithmetic mean is the sum of a set of values divided by the number of values. It is the most common measure of central tendency and is easy to calculate and understand. However, it can be heavily influenced by outliers, which can skew the mean and give a misleading representation of the data set. It is best used when the data is symmetrically distributed without extreme values and where there is compensability between the indicators.

The geometric mean is the nth root of the product of n values. It is particularly useful for data sets with values that are multiplicative or vary exponentially, such as growth rates. The geometric mean is less affected by extreme values compared to the arithmetic mean, providing a more accurate measure for skewed distributions. However, it is more complex to calculate and interpret, and it cannot be used with data sets containing zero or negative values.

Log transformation is a mathematical technique used to convert data to a logarithmic scale. This transformation helps in stabilizing variance, making the data more normally distributed, and reducing the impact of outliers. It is particularly useful for data sets with a wide range of values or exponential growth patterns.

# References

## Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Dottori, Francesco; Neal, Jeffrey; Prudhomme, Christel; Salamon, Peter (2024): Global River Flood Hazard Maps. European

# References

Commission, Joint Research Centre (JRC) [Dataset] PID: http://data.europa.eu/89h/jrc-floods-floodmapgl_rp50y-tif. Accessed 17 Mar. 2025

Copernicus Global Drought Observation. “Standard Precipitation Index.” EDO and GDO Indicator Factsheet. https://drought.emergency.copernicus.eu/data/factsheets/factsheet_spi.pdf. Accessed 17 Mar. 2025

CDRI (2023). Global Infrastructure Resilience: Capturing the resilience dividend - A Biennial Report from the Coalition for Disaster Resilient Infrastructure, New Delhi.

Dottori F; Salamon P; Alfieri L; Bianchi A; Feyen L; Hirpa F; Lorini V. Flood Hazard Maps at European and Global Scale. European Commission; 2016. JRC103765. https://publications.jrc.ec.europa.eu/repository/handle/JRC103765

Health Effects Institute. 2024. State of Global Air 2024. Special Report. Boston, MA: Health Effects Institute. https://www.stateofglobalair.org/resources/report/state-global-air-report-2024. Accessed 17 Mar 2025

IPCC, 2022: Climate Change 2022: Impacts, Adaptation and Vulnerability. Contribution of Working Group II to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [H.-O. Pörtner, D.C. Roberts, M. Tignor, E.S. Poloczanska, K. Mintenbeck, A. Alegría, M. Craig, S. Langsdorf, S. Löschke, V. Möller, A. Okem, B. Rama (eds.)]. Cambridge University Press. Cambridge University Press, Cambridge, UK and New York, NY, USA, 3056 pp., doi:10.1017/9781009325844.

Intergovernmental Panel on Climate Change. (2021). Climate Change 2021: The Physical Science Basis. Retrieved from https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-6/

Intergovernmental Panel on Climate Change. (2022). Climate Change 2022: Impacts, Adaptation and Vulnerability. Retrieved from https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-4/. Accessed 17 Mar 2025.

GIRI, 2023. Multi-hazard Disaster Risk Model of Infrastructure and Buildings at the Global Level (2023). Cardona, O.D., Bernal, G.A., Villegas, C.P., Molina, J.F., Herrera, S.A., Marulanda, M.C., Rincón, D.F., Grajales, S., Marulanda, P.M., Gonzalez, D., Maskrey, A. (2023). https://giri.unepgrid.ch/sites/default/files/2023-11/2.4-INGENIAR-CDRI-Background-Report-Risk-model.pdf. Accessed 17 Mar 2025.

MAP, 2025. Malaria Atlas Project. https://malariaatlas.org/. Accessed 17 Mar 2025.

OECD, 2008. Handbook on constructing composite indicators. Methodology and user guide – ISBN 978-92-64-04345. Accessed 17 Mar 2025.

Pfeffer, D.A., Lucas, T.C., May, D., Harris, J., Rozier, J., Twohig, K.A., Dalrymple, U., Guerra, C.A., Moyes, C.L., Thorn, M., Nguyen, M., et al. 2018. malariaAtlas: an R interface to global malariometric data hosted by the Malaria Atlas Project. Malaria Journal, 17(1), p.352

Reisinger, Andy, Mark Howden, Carolina Vera, et al. (2020) The Concept of Risk in the IPCC Sixth Assessment Report: A Summary of Cross-Working Group Discussions. Intergovernmental Panel on Climate Change, Geneva, Switzerland. pp15. https://www.ipcc.ch/site/assets/uploads/2021/02/Risk-guidance-FINAL_15Feb2021.pdf Accessed 17 Mar 2025

## Láng-Ritter, J., Keskinen, M. & Tenkanen, H. Global gridded population datasets systematically underrepresent rural population. Nat Commun 16, 2170 (2025). https://doi.org/10.1038/s41467-025-56906-7. Accessed 26 Mar 2025

# References

Shen, S. Li, C. van Donkelaar, A. Jacobs, N. Wang, C. Martin, R. V.: Enhancing Global Estimation of Fine Particulate Matter Concentrations by Including Geophysical a Priori Information in Deep Learning. (2024) ACS ES&T Air. DOI: 10.1021/acsestair.3c00054. Accessed 17 Mar 2025.

UNCCD 2024. “Global Sand and Dust Storm Base Map”. Technical Brief. https://www.unccd.int/sites/default/files/2024-10/UNCCD-WMO%20Technical%20Brief_SDS%20Source%20Base%20Map_Nov%202024.pdf. Accessed 17 Mar 2025.

UNICEF 2020. United Nations Children’s Fund, A Generation to Protect: Monitoring violence, exploitation and abuse of children within the SDG framework, UNICEF, New York, 2020. Accessed 17 Mar 2025.

United Nations Office for Disaster Risk Reduction. "Flood hazard and risk assessment." UNDRR, 2020. https://www.undrr.org/publication/flood-hazard-and-risk-assessment. Accessed 17 Mar 2025.

United Nations Office for Disaster Risk Reduction. "Flood." UNDRR, 2020. https://www.undrr.org/hips-cluster/flood. Accessed 17 Mar 2025.

United Nations Office for Disaster Risk Reduction. "Fluvial (Riverine) Flood." UNDRR, 2020. https://www.undrr.org/understanding-disaster-risk/terminology/hips/mh0007. Accessed 17 Mar 2025.

United Nations Office for Disaster Risk Reduction. "Drought." UNDRR, 2020. https://www.undrr.org/understanding-disaster-risk/terminology/hips/mh0035. Accessed 17 Mar 2025.

United Nations Food and Agriculture Organization. "Drought and Agriculture." FAO, 2020. https://www.fao.org/land-water/water/drought/droughtandag/en/. Accessed 17 Mar 2025.

United Nations Environment Programme. "Spreading like Wildfire: The Rising Threat of Extraordinary Landscape Fires." UNEP, 2022. https://www.unep.org/resources/report/spreading-wildfire-rising-threat-extraordinary-landscape-fires. Accessed 17 Mar 2025.

United Nations. "International Day of Combating Sand and Dust Storms." UN, 2023. https://www.un.org/en/observances/day-of-combating-sand-and-dust-storms. Accessed 17 Mar 2025.

United Nations Office for the Coordination of Humanitarian Affairs. "Extreme heat: Preparing for the heatwaves of the future." UN-OCHA, 2022. https://www.unocha.org/publications/report/world/extreme-heat-preparing-heatwaves-future-october-2022. Accessed 17 Mar 2025.

World Health Organization. "Malaria." WHO, 2024. https://www.who.int/en/news-room/fact-sheets/detail/malaria. Accessed 17 Mar 2025.

World Health Organization. "Air Pollution." WHO, 2024. https://www.who.int/news-room/fact-sheets/detail/air-pollution. Accessed 17 Mar 2025.

## WHO, 2021. World Health Organization global air quality guidelines. Particulate matter, ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide. Geneva: Licence: CCBY-NC-SA 2.0 IGO. https://www.who.int/publications/i/item/9789240034228. Accessed 17 Mar 2025.

# References

World Health Organization. (2024). Vector-borne diseases. Retrieved from https://www.who.int/news-room/fact-sheets/detail/vector-borne-diseases. Accessed 17 Mar 2025

Bondarenko M., Priyatikanto R., Zhang W., McKeen T., Cunningham A., Tejedor-Garavito N., Woods T., Hilton J., Cihan D., Nosatiuk B., Brinkhoff T., Tatem A., Sorichetta A. Unconstrained and constrained estimates of 2024 total number of people under the age of 18 per grid square at a resolution of 3 arc (approximately 100m at the equator), R2024A version v1.0 WorldPop, University of Southampton DOI: 10.5258/SOTON/WP00799

World Meteorological Organization. ‘Tropical Storm Classification.” https://wmo.int/content/classification-of-tropical-cyclones. Accessed 17 Mar 2025.

WMO, 2011. Manual on Flood Forecasting and Warning. WMO-No. 1072. World Meteorological Organization (WMO). Accessed 17 Mar 2025.

WMO, 2012. Definition number 543. International Glossary of Hydrology. WMO-No. 385. World Meteorological Organization (WMO). Accessed 17 Mar 2025.

WMO, 2025. Fires. Global Climate Observing System. https://gcos.wmo.int/site/global-climate-observing-system-gcos/essential-climate-variables/fire. Accessed 17 Mar 2025.

World malaria report 2024: addressing inequity in the global malaria response. Geneva: World Health Organization; 2024. License: CC BY-NC-SA 3.0 IGO.
