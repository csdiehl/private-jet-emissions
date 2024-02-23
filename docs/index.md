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
  <h1>Earthquakes</h1>
  <h2>This is a sample data viz about earthquakes</h2>

</div>

```js
const quakes = FileAttachment("data/quakes.csv").csv()
```

## Earthquakes

Here are some flights.

```js
Plot.plot({
  marks: [
    Plot.dot(quakes, { r: "magnitude", x: "longitude", y: 10, fill: "red" }),
  ],
})
```

Here is a plot of all the earthquakes.

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
    Plot.dot(quakes, {
      x: "longitude",
      y: "latitude",
      r: "magnitude",
      stroke: "#f43f5e",
    }),
  ],
})
```
