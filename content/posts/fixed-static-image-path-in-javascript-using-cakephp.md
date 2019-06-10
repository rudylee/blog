+++
date = "2010-11-10"
slug = "2010/11/10/fixed-static-image-path-in-javascript-using-cakephp"
title = "Fixed static image path in Javascript using CakePHP"
Categories = ["CakePHP"]
Tags = ["CakePHP", "javascript", "router"]
+++

Today I was encountered a problem within the static path for images in my Javascript file. So this was a design that given by my friend Budi, and he using a Jquery slider plugin in his design. Here are the original Javascript file that he gave me :

    
``` javascript
// set up horizontal scroll
var setupFeaturedBoxes = function () {
  var buttons = {
    previous: {
      enabled: '/img/arrow1-left.gif',
      hover: '/img/arrow1-left.gif'
    },
    next: {
      enabled: '/img/arrow1-right.gif',
      hover: '/img/arrow1-right.gif'
    }
  };

  var featuredContentWidth = 121;
  var featuredContentScrollPrefs = {
    speed: 800,
    axis: 'x'
  };

jQuery('.featuredBox').each( function (i) {
  var featuredBox = jQuery(this);
  featuredBox
  .find('.scrollArrow')
  .filter('.next')
  .hover(
  function () {
  jQuery(this)
    .attr( 'src', buttons.next.hover )
    .css( 'cursor', 'pointer' );
  },
  function () {
    jQuery(this)
      .attr( 'src', buttons.next.enabled )
      .css( 'cursor', 'default' );
    }
  )
.click( function() {
  featuredBox.find('.featuredContent').scrollTo(
  '+=' + featuredContentWidth + 'px',
  featuredContentScrollPrefs
);
  return false;
})
.end()
.filter('.prev')
.hover(
function () {
  jQuery(this)
    .attr( 'src', buttons.previous.hover )
    .css( 'cursor', 'pointer' );
  },
function () {
jQuery(this)
  .attr( 'src', buttons.previous.enabled )
  .css( 'cursor', 'default' );
}
)
.click( function() {
featuredBox.find('.featuredContent').scrollTo(
  '-=' + featuredContentWidth + 'px',
  featuredContentScrollPrefs
);
  return false;
});
});
  jQuery('.featuredBox .featuredContent .featuredDisplayDiv').each( function (i) {
  jQuery(this).css( 'width', ( featuredContentWidth * jQuery(this).find('ul li').size() ) + 'px' );
});
};

var setupFeaturedBoxes2 = function () {
var buttons = {
previous: {
  enabled: '/img/arrow2-left.gif',
  hover: '/img/arrow2-left.gif'
},
next: {
  enabled: '/img/arrow2-right.gif',
  hover: '/img/arrow2-right.gif'
}
};
  var featuredContentWidth2 = 172;
  var featuredContentScrollPrefs = {
    speed: 800,
    axis: 'x'
  };
  jQuery('.featuredBox2').each( function (i) {
  var featuredBox = jQuery(this);
  featuredBox
  .find('.scrollArrow')
  .filter('.next')
  .hover(
  function () {
    jQuery(this)
      .attr( 'src', buttons.next.hover )
      .css( 'cursor', 'pointer' );
    },
  function () {
    jQuery(this)
      .attr( 'src', buttons.next.enabled )
      .css( 'cursor', 'default' );
    }
  )
  .click( function() {
  featuredBox.find('.featuredContent2').scrollTo(
    '+=' + featuredContentWidth2 + 'px',
    featuredContentScrollPrefs
  );
    return false;
  })
  .end()
  .filter('.prev')
  .hover(
  function () {
    jQuery(this)
    .attr( 'src', buttons.previous.hover )
    .css( 'cursor', 'pointer' );
  },
  function () {
    jQuery(this)
      .attr( 'src', buttons.previous.enabled )
      .css( 'cursor', 'default' );
    }
  )
  .click( function() {
    featuredBox.find('.featuredContent2').scrollTo(
      '-=' + featuredContentWidth2 + 'px',
      featuredContentScrollPrefs
    );
      return false;
    });
  });
  jQuery('.featuredBox2 .featuredContent2 .featuredDisplayDiv2').each( function (i) {
    jQuery(this).css( 'width', ( featuredContentWidth2 * jQuery(this).find('ul li').size() ) + 'px' );
  });
};


jQuery(document).ready(function(){
  // set up horizontal scroll
  setupFeaturedBoxes();
  setupFeaturedBoxes2();
});
```

As you can see at the line 5 there is an image path in which needed by the slider to load the image. Actually I can easily using the absolute path but if change the environment or the path then the image will be broken. So here come the Router class of CakePHP to the rescue.

The idea is to change the Javascript file to PHP file and change the path to use the Router class. Here is the sample of my PHP file :


``` javascript
    <script type="text/javascript" language="JavaScript">
    var setupFeaturedBoxes = function () {
    	var buttons = {
    		previous: {
    			enabled: <?php Router::url('/img/arrow1-left.gif')?>,
    			hover: <?php Router::url('/img/arrow1-left.gif')?>
    		},
    		next: {
    			enabled: <?php Router::url('/img/arrow1-right.gif')?>,
    			hover: <?php Router::url('/img/arrow1-right.gif')?>
    		}
    	};
    	var featuredContentWidth = 121;
    	var featuredContentScrollPrefs = {
    		speed: 800,
    		axis: 'x'
    	};
    	jQuery('.featuredBox').each( function (i) {
    		var featuredBox = jQuery(this);
    		featuredBox
    			.find('.scrollArrow')
    				.filter('.next')
    					.hover(
    						function () {
    							jQuery(this)
    								.attr( 'src', buttons.next.hover )
    								.css( 'cursor', 'pointer' )
    							;
    						},
    						function () {
    							jQuery(this)
    								.attr( 'src', buttons.next.enabled )
    								.css( 'cursor', 'default' )
    							;
    						}
    					)
    					.click( function() {
    						featuredBox.find('.featuredContent').scrollTo(
    							'+=' + featuredContentWidth + 'px',
    							featuredContentScrollPrefs
    						);
    						return false;
    					})
    				.end()
    				.filter('.prev')
    					.hover(
    						function () {
    							jQuery(this)
    								.attr( 'src', buttons.previous.hover )
    								.css( 'cursor', 'pointer' )
    							;
    						},
    						function () {
    							jQuery(this)
    								.attr( 'src', buttons.previous.enabled )
    								.css( 'cursor', 'default' )
    							;
    						}
    					)
    					.click( function() {
    						featuredBox.find('.featuredContent').scrollTo(
    							'-=' + featuredContentWidth + 'px',
    							featuredContentScrollPrefs
    						);
    						return false;
    					})
    		;
    	});
    	jQuery('.featuredBox .featuredContent .featuredDisplayDiv').each( function (i) {
    		jQuery(this).css( 'width', ( featuredContentWidth * jQuery(this).find('ul li').size() ) + 'px' );
    	});
    };
    
    var setupFeaturedBoxes2 = function () {
    	var buttons = {
    		previous: {
    			enabled: <?php Router::url('/img/arrow2-left.gif')?>,
    			hover: <?php Router::url('/img/arrow2-left.gif')?>
    		},
    		next: {
    			enabled: <?php Router::url('/img/arrow2-right.gif')?>,
    			hover: <?php Router::url('/img/arrow2-right.gif')?>
    		}
    	};
    	var featuredContentWidth2 = 172;
    	var featuredContentScrollPrefs = {
    		speed: 800,
    		axis: 'x'
    	};
    	jQuery('.featuredBox2').each( function (i) {
    		var featuredBox = jQuery(this);
    		featuredBox
    			.find('.scrollArrow')
    				.filter('.next')
    					.hover(
    						function () {
    							jQuery(this)
    								.attr( 'src', buttons.next.hover )
    								.css( 'cursor', 'pointer' )
    							;
    						},
    						function () {
    							jQuery(this)
    								.attr( 'src', buttons.next.enabled )
    								.css( 'cursor', 'default' )
    							;
    						}
    					)
    					.click( function() {
    						featuredBox.find('.featuredContent2').scrollTo(
    							'+=' + featuredContentWidth2 + 'px',
    							featuredContentScrollPrefs
    						);
    						return false;
    					})
    				.end()
    				.filter('.prev')
    					.hover(
    						function () {
    							jQuery(this)
    								.attr( 'src', buttons.previous.hover )
    								.css( 'cursor', 'pointer' )
    							;
    						},
    						function () {
    							jQuery(this)
    								.attr( 'src', buttons.previous.enabled )
    								.css( 'cursor', 'default' )
    							;
    						}
    					)
    					.click( function() {
    						featuredBox.find('.featuredContent2').scrollTo(
    							'-=' + featuredContentWidth2 + 'px',
    							featuredContentScrollPrefs
    						);
    						return false;
    					})
    		;
    	});
    	jQuery('.featuredBox2 .featuredContent2 .featuredDisplayDiv2').each( function (i) {
    		jQuery(this).css( 'width', ( featuredContentWidth2 * jQuery(this).find('ul li').size() ) + 'px' );
    	});
    };
    
    
    jQuery(document).ready(function(){
    
    
    // set up horizontal scroll
    	setupFeaturedBoxes();
    	setupFeaturedBoxes2();
    
    });
</script>
```
    


As you can see I just change the image path to . I don't know if this is the best solution or not, but for now it's the simplest :D 
