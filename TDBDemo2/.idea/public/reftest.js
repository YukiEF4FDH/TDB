// import * as Vue from 'vue';

const ReferenceTemplate = `
<span class="reference" :reference_id="this.id" @mouseover="setHover($event)"><slot></slot></span>
`;

const app = Vue.createApp({})

let reference_id = 0;

app.component('ref', {
	data() {
		return {
			id: 0,
			text: 'default'
		}
	},
	created() {
		this.id = reference_id++; // data.id更新

		const _default = this.$slots.default();
		if (_default && _default.length > 0)
			this.text = _default[0].children; // data.text更新
	},

	template: ReferenceTemplate,

	methods: {
		setHover: function (ev) {
			d3.select(document.getElementById("rect_0")).attr("fill", "yellow");
		},
		setLeave: function (ev) {
		},
	}
});

app.mount('#app');