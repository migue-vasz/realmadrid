function Mostar(var1,var2,color)
{
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++)
  {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++)
  {
    tablinks[i].style.backgroundColor = "";
  }
  document.getElementById(var1).style.display = "block";
  var2.style.backgroundColor = color;
}
document.getElementById("IAbierto").click();
