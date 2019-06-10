+++
date = "2011-07-25"
slug = "2011/07/25/jquery-ui-autocomplete-in-cakephp"
title = "jQuery UI AutoComplete in CakePHP"
Categories = ["CakePHP"]
Tags = ["ajax", "apps", "array", "autocomplete", "CakePHP", "callback", "field options", "jquery", "little bit", "pl", "return string", "script check", "source options", "string field", "unset", "url options"]
+++

 
 
## Demo : [http://cbunny.rudylee.com/autocomplete](http://cbunny.rudylee.com/autocomplete)
## Demo source code :[ https://github.com/rudylee/cbunny]( https://github.com/rudylee/cbunny)

The post to add auto redirect feature into the AutoComplete : [http://blog.rudylee.com/2011/12/12/auto-redirect-in-cakephp-jquery-autocomplete/](http://blog.rudylee.com/2011/12/12/auto-redirect-in-cakephp-jquery-autocomplete/)
You can copy the modified Ajax and Javascript helpers from here [https://github.com/rudylee/topping](https://github.com/rudylee/topping)

Last week I was trying to use [jQuery UI Autocomplete](http://jqueryui.com/demos/autocomplete/) in my CakePHP apps. However, CakePHP Ajax and Javascript helpers don't support jQuery by default. After googling a little bit, I found that this guy ( [http://www.cakephp.bee.pl/](http://www.cakephp.bee.pl/) ) already made Ajax and Javascript helpers for jQuery.

So I just copied these helpers from his site and put it into my apps. It's done ? obviously not. It turned out that the autocomplete script that he using in his helper is the old one ( [http://docs.jquery.com/Plugins/autocomplete](http://docs.jquery.com/Plugins/autocomplete) ).

Thus, I had to add a method inside that helper to use jQuery UI autocomplete. Here are the sample codes ( you can copy from my github for the complete file, this one is just snippet ) :

``` php    
/**
 * Options for auto-complete editor.
 *
 * @var array
 */
var $autoCompleteOptions = array(
    'select', 'source'
);

/**
 * Create a text field with Jquery UI Autocomplete.
 *
 * Creates an autocomplete field with the given ID and options.
 * needs include jQuery UI Autocomplete file
 *
 * @param string $field DOM ID of field to observe
 * @param array $options Ajax options
 * @return string Ajax script
 * check out http://jqueryui.com/demos/autocomplete/
 */
function autoComplete($field, $options = array()) {
    $var = '';
    if (isset($options['var'])) {
        $var = 'var ' . $options['var'] . ' = ';
        unset($options['var']);
    }

    if(isset($options['source'])) {
        $options['source'] = "'".Router::url($options['source'])."'";
    }

    if (!isset($options['id'])) {
        $options['id'] = Inflector::camelize(str_replace(".", "_", $field));
    }

    $htmlOptions = $this->__getHtmlOptions($options);
    $htmlOptions['autocomplete'] = "off";

    foreach ($this->autoCompleteOptions as $opt) {
        unset($htmlOptions[$opt]);
    }

    $options = $this->_optionsToString($options, array('multipleSeparator'));
    $callbacks = array('formatItem', 'formatMatch', 'formatResult', 'highlight');

    foreach ($callbacks as $callback) {
        if (isset($options[$callback])) {
            $name = $callback;
            $code = $options[$callback];
            switch ($name) {
                case 'formatResult':
                    $options[$name] = "function(data, i, max) {" . $code . "}";
                    break;
                case 'highlight':
                    $options[$name] = "function(data, search) {" . $code . "}";
                    break;
                default:
                    $options[$name] = "function(row, i, max, term) {" . $code . "}";
                    break;
            }
        }
    }
    $options = $this->_buildOptions($options, $this->autoCompleteOptions);

    $text = $this->Form->text($field, $htmlOptions);
    $script = "{$var} $('#{$htmlOptions['id']}').autocomplete(";
    $script .= "{$options});";

    return "{$text}\n" . $this->Javascript->codeBlock($script);
}
```


And here are the sample to use it in our application

``` php    
echo $this->Ajax->autoComplete('Guest.search', array(
    'source' => array(
        'controller' => 'users',
        'action' => 'autoComplete',
        'prefix' => 'host'
    ),
));
```

Action code :

``` php
/**
 * Auto Complete Action for Host
 *
 * Auto Complete action for host list of guests
 * also process the search
 */
function host_autoComplete() {
    if (!empty($this->data)) {
        $this->redirect(array(
            'controller' => 'users',
            'action' => 'view', $this->data['Guest']['id']
        ));
    }
    $this->autoRender = false;
    $guests = $this->User->getGuests(array(
        'host_id' => Configure::read('User.id'),
            'conditions' => array(
                'OR' => array(
                'User.name LIKE' => '%' . $_GET['term'] . '%',
                'User.surname LIKE' => '%' . $_GET['term'] . '%'
            )
        )
    ));
    echo json_encode($this->User->autoComplete_encode($guests));
}
```

Model method ( encode the data array to display fields that we want, in this example I am just showing firstname and surname )

``` php    
/**
 * autoComplete encode
 *
 * Parsing passed array and change it to consume-able
 * by autocomplete jQuery UI
 * @param array $data
 * @return json $data
 */
function autoComplete_encode($postData = array()) {
    $temp = array();
    foreach ($postData as $user) {
        array_push($temp, array(
            'id' => $user['User']['id'],
            'label' => $user['User']['name'].' '.$user['User']['surname'],
            'value' => $user['User']['name'],
        ));
    }
    return $temp;
}
```

Don't forget to use $_GET['term'] to get data from autocomplete field and also encode the data to JSON so it can be displayed by jQuery UI.
