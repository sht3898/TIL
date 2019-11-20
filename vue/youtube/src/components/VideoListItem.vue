<template>
  <li @click="selectedVideo" class="list-group-item my-3 py-3">
      <img :src="video.snippet.thumbnails.high.url" :alt="video.snippet.title">
      <h3>{{ video.snippet.title }}</h3>
      <p>{{ video.snippet.description }}</p>
  </li>
</template>

<script>

export default {
    name: 'VideoListItem',
    props: {
        video: {
            type: Object,
            required: true
        }
    },
    methods: {
        selectedVideo() {
            // video-select-event
            console.log(this.video)
            // 자식 컴포넌트에서는 이벤트 발생(값 전달0)
            this.$emit('video-select-event', this.video)
        }
    }
}
</script>

<style scoped>
/* scoped : 해당 컴포넌트에서만 사용되는 style */
img {
    width: 360px;
}
li {
    cursor: pointer
}
li:hover {
    background-color: #fffff2;
}
</style>