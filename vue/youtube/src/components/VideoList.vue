<template> <!-- template는 반드시 하나의 div만 가질 수 있다. 하나로 묶고 시작하기. --> 
  <div>
      <h2>영상 목록</h2>
      <ul class="list-group">
          <video-list-item
            :video="video" 
            v-for="video in videos" 
            :key="video.id.videoId"
            @video-select-event="selectedVideo"
          ></video-list-item>
          <!-- 부모 컴포넌트에서는 이벤트 listen(v-on)
            => 원하는 메서드 실행
           -->
      </ul>
  </div>
  <!-- <div></div> => error -->
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default { 
    name: 'VideoList',
    components: {
        VideoListItem
    },
    props: {
        videos: {
            type: Array,
            required: true
        }
    },
    methods: {
        selectedVideo(video) {
            console.log('리스트로 할당!')
            this.$emit('video-select-event', video)
        }
    }
}
</script>

<style>

</style>