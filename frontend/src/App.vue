<template>
  <div>
    <div v-for="name in tables" :key="name">
      <form action="/api/get_csv_table" method="post">
        <input type="text" name="table_name" :value="name" hidden>
        <button type="submit">Скачать {{name}}</button>
      </form>
    </div>
    <ul>
      <li v-for="user in users" :key="user">{{ user }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "",
      tables: ['location_types', 'locations', 'air_measurments', 'country_codes_adjacent',
        'areas_and_densities', 'crop_production', 'populations', 'blocks_and_roads',
        'energy_consumption', 'trends', 'co2_emission'
      ]
    };
  },

  mounted() {
    /*
    fetch("/api")
      .then((response) => response.text())
      .then((data) => {
        this.message = data;
      });
      */
  },
};
</script>