using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour {
    // Gildi og breytur hér
    public int lives; 
    public int gems; 
    public Text lifeText; 
    public Text gemText;
    public bool gameOver;
    public Transform Respawn; // Checkpoint sem player mun fara ef hann deyr
    public Transform VictoryScreen; //Sýnir þetta ef þú klárar demo
    public GameObject gameOverPanel;
    public GameObject winningPanel;

    void Start () {
        lifeText.text = "Lives: " + lives;
        gemText.text = "Gems: " + gems;
	}
	
    public void GemCount() //Bætir við stigi
    {
        gems++;
        gemText.text = "Gems: " + gems;
    }


    public void UpdateLives(int ChangeInLives) //Fall sem uppfærir lífin eftir því hvort player fær líf eða missir þau og svo fer í gameOver þegar hann er dauður
    {
        lives += ChangeInLives;

        if (lives <= 0)
        {
            lives = 0;
            TriggerGameOver();
        }


        lifeText.text = "Lives: " + lives; //Birtir lífin í gameover textanum
    }

    void TriggerGameOver() //Kveikir á GameOver panel
    {
        gameOver = true;

        gameOverPanel.SetActive(true);
        
    }

    public void TriggerWin() //Kallar á fallið þegar búinn er að vinna
    {
        gameOver = true;

        winningPanel.SetActive(true);

    }

    public void RestartGame() // Endurræsa leikinn ef einhver ýtir á restart takkann
    {
        SceneManager.LoadScene("Verkefni2Scene");
    }

    public void ExitGame() //Hættir leiknum ef player ýtir á þetta
    {
        Application.Quit();
    }


}
