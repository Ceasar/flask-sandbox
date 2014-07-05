$( "form" ).on( "submit", function( event ) {
  console.log( $( this ).serialize() );
});
