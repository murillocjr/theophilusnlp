let dvconfig = {
    create: function () {
        return {
            default_link_distance: 10,

            // How far can we change default_link_distance?
            // 0   - I don't care
            // 0.5 - Change it as you want, but it's preferrable to have default_link_distance
            // 1   - One does not change default_link_distance
            // 0.7
            default_link_strength: 0,

            // Should I comment this?
            default_circle_radius: 15,

            // you can set it to true, but this will not help to understanf what's going on
            show_texts_near_circles: true,

            default_max_texts_length: 100,

            // 200
            charge_multiplier: 0,
            // power link
            link_pow : 3,
            link_coe : 1000,

            max_distance: 0.9
        }
    }
};
