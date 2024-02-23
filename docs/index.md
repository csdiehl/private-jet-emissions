---
toc: false
---

<style>

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
  background: linear-gradient(30deg, var(--theme-foreground-focus), red);
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

## Private Jet Emissions

Every few months celebrities face intense scrutiny on social media for their private jet usage. But a much longer list of business executives, public figures, and politicians indulge in luxury travel. Although corporate activity, rather than personal consumption, accounts for most emissions, these people emit more than some enterprises and large swaths of the general public.

Forbes lists about 2,095 billionaires. Their outsize emissions mainly stem from transportation. The super-wealthy maintain fleets of private jets, superyachts and other vehicles. A single superyacht produces emissions equal to the total consumption pattern of 167 average American households. Elon Musk took at least 114 private jet flights in 2023, which emits at least 285 times more carbon in that year than the average American flying commercial.

## Who flew the most?

Let's look at who took the most private jet flights in 2023.

```js
Plot.plot({
  marginLeft: 100,
  marks: [
    Plot.barX(flightsByOwner.slice(0, 20), {
      x: "flights",
      y: "owner",
      sort: { y: "-x" },
    }),
  ],
})
```

## Who spent the most time flying?

Here are the people who spent the most time in the air.

```js
Plot.plot({
  marginLeft: 100,
  marks: [
    Plot.barX(sortedPpl, {
      x: "total_time_hrs",
      y: "owner",
      sort: { y: "-x" },
    }),
  ],
})
```

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

## Where are they going?

Here is a plot of flights around the world.

```js
Plot.plot({
  projection: {
    type: "orthographic",
    rotate: [110, -30],
  },
  marks: [
    Plot.graticule(),
    Plot.sphere(),
    // Plot.geo(land, { stroke: "var(--theme-foreground-faint)" }),
  ],
})
```

## What are they flying in?

Here are the most popular aircraft types. Some of the most popular manufacturers include Dassault and Bombardier.

```js
Inputs.table(aircraft)
```
