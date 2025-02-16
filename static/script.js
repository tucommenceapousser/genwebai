// Attendre que le DOM soit complètement chargé avant d'ajouter les événements
document.addEventListener('DOMContentLoaded', function() {

  // Sélectionner les boutons par leur classe
  const btnPrimary = document.querySelector('.primary');
  const btnSecondary = document.querySelector('.secondary');
  const previewBox = document.getElementById('preview-box');

  // Ajouter un événement au bouton "HTML/CSS/JS"
  btnPrimary.addEventListener('click', function() {
    previewBox.innerHTML = '<p>Prévisualisation d\'un site HTML/CSS/JS...</p>';
    console.log('Bouton HTML/CSS/JS cliqué');
  });

  // Ajouter un événement au bouton "Web Flask"
  btnSecondary.addEventListener('click', function() {
    previewBox.innerHTML = '<p>Prévisualisation d\'un site Flask...</p>';
    console.log('Bouton Web Flask cliqué');
  });
});
