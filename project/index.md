---
toc: false
---

<style>

:root {
  --main-color: #53d8fb;
}

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  margin: 4rem 0 8rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 2rem 0;
  max-width: none;
  font-size: 14vw;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(30deg, var(--theme-foreground-focus), var(--main-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero h2 {
  margin: 0;
  max-width: 34em;
  font-size: 20px;
  font-style: initial;
  font-weight: 500;
  line-height: 1.5;
  color: var(--theme-foreground-muted);
}

@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}

html, body {
    font-family: sans-serif;
}

h2 {
  color: var(--main-color);
}

p {
  opacity: .8;
}

.intro {
  height: 80vh;
  flex-direction: column;
  display: flex;
  align-items: center;
  }

  section {
    margin: 0 0 80px;
  }

  select {
    height: 48px;
    border-radius: 10px;
    padding: 0 16px;
    color: #FFF;

  }

  #selector {
    display: flex;
    justify-content: space-between;
  }

</style>

<div class="hero">
  <h1>Private Jet Emissions</h1>
  <h2>and why they are bad</h2>

</div>

```js
const flightsByOwner = await FileAttachment("data/flights.csv").csv({
  typed: true,
})

const od = await FileAttachment("data/od.csv").csv({
  typed: true,
})

const aircraft = await FileAttachment("data/aircraft.csv").csv({
  typed: true,
})

const sortedPpl = flightsByOwner
  .toSorted((a, b) => b.total_time_hrs - a.total_time_hrs)
  .slice(0, 20)
```

<div class='intro'>
<div>
<h2>Private Jet Emissions</h2>
<p>Every few months celebrities face intense scrutiny on social media for their private jet usage. But a much longer list of business executives, public figures, and politicians indulge in luxury travel. Although corporate activity, rather than personal consumption, accounts for most emissions, these people emit more than some enterprises and large swaths of the general public.</p>
<p>Forbes lists about 2,095 billionaires. Their outsize emissions mainly stem from transportation. The super-wealthy maintain fleets of private jets, superyachts and other vehicles. A single superyacht produces emissions equal to the total consumption pattern of 167 average American households. Elon Musk took at least 114 private jet flights in 2023, which emits at least 285 times more carbon in that year than the average American flying commercial.</p>
</div>
</div>

<section>
<h2>Who flew the most?</h2>
<p>Let's look at who took the most private jet flights in 2023.</p>
<div class="card">
${Plot.plot({
  marginLeft: 100,
  marks: [
    Plot.barX(flightsByOwner.slice(0, 20), {
      x: "flights",
      y: "owner",
      sort: { y: "-x" },
    }),
  ],
})}
</div>
</section>

```js
await visibility()

const flights = await FileAttachment("./data/2023_flights_geodata.json").json()
const landData = await fetch(
  "https://cdn.jsdelivr.net/npm/world-atlas@2/land-110m.json"
).then((d) => d.json())

const land = topojson.feature(landData, landData.objects.land)

const flightsGeo = topojson.feature(
  flights,
  flights.objects["2023_flights_geodata"]
)

const personInput = html`<select id="ppl-select">
  <option value="Elon Musk">Elon Musk</option>
  <option value="Jeff Bezos">Jeff Bezos</option>
  <option value="Lawrence Stroll">Lawrence Stroll</option>
</select>`
const person = Generators.input(personInput)
```

<section>
<div id='selector'>
<h2>Where is ${person} going?</h2>
${personInput}
</div>
<div>
${Plot.plot({
  width: width,
  projection: {
    type: "orthographic",
    rotate: [60, -40],
  },
  marks: [
    Plot.graticule(),
    Plot.sphere(),
    Plot.geo(land, { stroke: "white", opacity: 0.5 }),
    Plot.geo(flightsGeo, {
      filter: (d) => d.properties.owner == person,
      stroke: "#53d8fb",
      opacity: 0.3,
    }),
  ],
})}
</div>
</section>

## Who spent the most time flying?

Total time spent flying is clearly correlated with the number of trips taken. Some of the people who took the most trips also spent the longest in the air.

```js
Plot.plot({
  width: width,
  height: 500,
  grid: true,
  marks: [
    Plot.dot(flightsByOwner, {
      x: "total_time_hrs",
      y: "flights",
    }),
    Plot.text(flightsByOwner.slice(0, 20), {
      x: "total_time_hrs",
      y: "flights",
      text: (d) => d.owner,
      fill: "#FFF",
      dy: -6,
    }),
  ],
})
```

## Many of these flights are short hops that replace car trips.

It's particularly alarming that many flights are 30 minutes or less.

Most flights are under an hour or two. It's rare for flights to be over 3hrs.

## What are they flying in?

Here are the most popular aircraft types. Some of the most popular manufacturers include Dassault and Bombardier.

<div class='card'>
${Inputs.table(aircraft)}
</div>
