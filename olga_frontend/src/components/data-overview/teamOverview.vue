<template>
  <div>
    <b-tab title="Team Data">
      <b-card>
        <h4>Team members</h4>
        <div>
          <b-button v-b-toggle.collapse-1 variant="primary"
            >show members</b-button
          >
          <b-collapse id="collapse-1" class="mt-2">
            <b-card>
              <p class="card-text">(Members Listed)</p>
            </b-card>
          </b-collapse>
        </div>
      </b-card>
      <TeamTable />
    </b-tab>
  </div>
</template>

<script>
import TeamTable from "@/components/data-detail/teamTable.vue";

export default {
  name: "TeamOverview",
  components: {
    TeamTable
  }
};
</script>

<style lang="scss" scoped></style>
