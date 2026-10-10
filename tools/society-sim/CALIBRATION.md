# Calibration: keeping the simulated world near the real one

The simulation's agents act on probability weights. Left alone, a small synthetic population drifts: a run can end with nine in ten adults unemployed, no marriages for a decade, or an age pyramid no census has ever seen. Calibration is the mechanism that turns the weights so that the rates the simulation produces stay near the rates Singapore publishes, without ever touching a fact or a law.

## The one rule

**Calibration adjusts intentions, never outcomes.** It may raise or lower the chance that a person seeks a job or that an employer hires, that a couple tries for a child, that a company is formed. It may never set a fact, and it may never change what the law does about an act. Those two constraints are what keep a calibrated run in Nature mode: everything that happens still happens through somebody's act, and every consequence still comes from an L4 row. A calibrated run is therefore still evidence; an edited one would not be.

## Targets

A target is a published rate, by stratum, with provenance.

| target | strata | source |
| --- | --- | --- |
| live births per 1,000 women | mother's age band | SingStat, Population Trends; Registry of Births and Deaths annual report |
| deaths per 1,000 | age band and sex | SingStat life tables |
| marriages per 1,000 unmarried residents | age band | SingStat, Statistics on Marriages and Divorces |
| employment rate; monthly job separations and hires | age band, sex | MOM Labour Force in Singapore, Labour Market Report |
| median gross monthly income | age band | MOM Comprehensive Labour Force Survey |
| HDB and private home ownership; resale and BTO transactions per year | household type | HDB Annual Report; URA |
| company incorporations and strike-offs per year | — | ACRA |
| net migration; new citizens and PRs per year | age band | SingStat, Population in Brief |
| household size; persons per flat | flat type | Census, General Household Survey |

Targets live in `tools/society-sim/targets/` as CSV, one file per rate, each row carrying the year it describes and the publication it came from. A target without provenance is not a target. Where the real figure is for the whole resident population and the simulation's population is a subset (citizens only, say), the target file says which denominator it uses.

## Observations

The simulation already counts things. Calibration reads the same counters over a trailing window and computes the same rates by the same strata as the targets. The window is long enough to see past noise: a population of a few hundred produces single-digit events a year in most strata, so a twelve-month window is the minimum and thirty-six months is safer for births and deaths. The checker refuses a target whose stratum would hold fewer than a set number of actors, because a rate over three people is not a rate.

## The controller

For each target and stratum, one knob: the base chance in the generator that produces the intention. Once a simulated month, for each knob:

1. Compute the observed rate over the window and the target for that year.
2. If the observed rate is inside the tolerance band (ten per cent of the target by default, wider for rare events), do nothing.
3. Otherwise multiply the knob by (target ÷ observed) raised to a gain below one, so that the correction is partial, and clamp the change to a maximum factor per step. Proportional in log space, damped, bounded. Nothing cleverer is needed until the data say so.
4. Log the adjustment: date, knob, observed, target, old value, new value, and the window used.

The controller is deterministic given the seed and the targets, so a calibrated run replays exactly. It never runs inside a day step; it runs between months, and the sandpit forks inherit the knobs they were forked with and keep calibrating on their own clock.

## Saturation is a finding

A knob has limits. If the controller pins one at its ceiling or floor for more than a few months, calibration has failed to close the gap, and that is information:

- **A law gap.** Nine in ten unemployed with the hiring knob at its ceiling usually means hiring attempts are failing in adjudication, because the Employment Act row refuses, or a required instrument is missing and the taint is blocking the consequence. The requirement ledger will already have the entry; the saturation tells you its weight.
- **A model gap.** The agents may lack an intention the real population has. Nobody in the simulation migrates in, so the population ages out; nobody forms a company because no profile wants to.
- **A target gap.** The published rate and the simulated denominator do not match.

Saturations go to a calibration log beside the adjustment log, with the knob, the duration and the controller's best guess at the cause, and the dashboard shows them. They are not written to the requirement ledger unless the cause is a missing encoding, and then the ledger entry gains a count, not a new line.

## Structure, not only rates

Rates alone will not hold the shape of the population. Three structural levers:

- **Immigration and emigration.** The population cap is a hard maximum, but a population held only by births and deaths ages into a pyramid Singapore does not have. New adults arrive by immigration at the published net rate, as acts under the Immigration Act and the Constitution's citizenship provisions, both of which have rows. Emigration is the symmetric act.
- **Cohort targets where they exist.** Age-specific fertility beats total fertility; age-specific marriage rates beat the crude rate. Where only a cross-sectional figure is published, use it and say so in the target file.
- **A census every simulated decade.** The Census Act and the Statistics Act rows already model the duty to answer. Run the simulated census on the real census years and compare the tables to the real ones. That is the slow, structural check the monthly controller cannot make.

## Real-time mode

With the clock locked to the wall, targets are the latest published figures and the window trails behind real time. When SingStat publishes a new year, the target file gains a row and the controller follows it. The population is larger, so strata are better populated and the tolerance bands can be tighter.

## What is deliberately left out

- No optimiser fitting many knobs at once. One knob per rate, adjusted independently, is explainable; a joint fit is not, and explainability is the point of the whole simulation.
- No calibration of legal outcomes. If the simulated offence rate is wrong, the cause is in the intentions or the law, and the fix is there.
- No adjustment inside a day. The world a day sees is fixed when the day starts.
