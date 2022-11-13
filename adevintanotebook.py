{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "NJDJqKc8wH_P"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('events_log.csv')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#1"
      ],
      "metadata": {
        "id": "aBYFRSQhwVtb"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "a) What is our daily overall clickthrough rate?"
      ],
      "metadata": {
        "id": "gBjjutGRwPn8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Entries where user visited any of the displayed search results\n",
        "ct_df = df[df['action'] == 'visitPage']\n",
        "\n",
        "# overall click-through rate\n",
        "overall_ct_rate = len(ct_df) / len(df) *100\n",
        "print('over all click-through rate is : {:.3f}'.format(overall_ct_rate))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "05s2kDJswQ4l",
        "outputId": "15d794ed-121f-47f3-d3e3-85a11c7cbd12"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "over all click-through rate is : 10.023\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "b) How does it vary between the groups?"
      ],
      "metadata": {
        "id": "OAq_AMvGwcFn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for group_name, group_df in df.groupby(by='group'):\n",
        "    ct_group_df = group_df[group_df['action'] == 'visitPage']\n",
        "    group_ct_rate = len(ct_group_df) / len(group_df) *100\n",
        "    print('Group click-through rate for Group ({}) is : {:.3f}'.format(group_name, group_ct_rate))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N29E4j9cweRR",
        "outputId": "f0ad2625-4592-4dcb-9379-ce95c2cc0950"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Group click-through rate for Group (a) is : 11.125\n",
            "Group click-through rate for Group (b) is : 6.764\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#2"
      ],
      "metadata": {
        "id": "ITLxoDFUwhhB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "a) Which results do people tend to try first?"
      ],
      "metadata": {
        "id": "n9c7EYbQwi0a"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('The results at position No : {} are most likely to be tried first'.format(int(df['result_position'].mode())))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KfAz8s2fwl9g",
        "outputId": "34da03c1-7cd1-4dbb-e3a3-80d89ceb5610"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The results at position No : 1 are most likely to be tried first\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "b) How does it change day-to-day?"
      ],
      "metadata": {
        "id": "PbTMZAK0wwi4"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "uzBB6wSdw0pR"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#3"
      ],
      "metadata": {
        "id": "yt_L4IPFw1Yw"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "a) What is our daily overall zero results rate?"
      ],
      "metadata": {
        "id": "7zrxQMYSw24F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "oz_df = df[df['n_results'] == 0.0]\n",
        "\n",
        "oz_rate = len(oz_df) / len(df) * 100\n",
        "print('over all zero result rate is : {:.3f}'.format(oz_rate))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_OTcPqfWw7H4",
        "outputId": "037a75e9-6df8-4fa1-ff6b-6f00fdedfa71"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "over all zero result rate is : 6.279\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "How does it vary between the groups?"
      ],
      "metadata": {
        "id": "US1Y6YZUxA4w"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for group_name, group_df in df.groupby(by='group'):\n",
        "    oz_group_df = group_df[group_df['n_results'] == 0.0]\n",
        "    group_oz_rate = len(oz_group_df) / len(group_df) * 100\n",
        "    print('Group Zero-result rate for Group ({}) is : {:.3f}'.format(group_name, group_oz_rate))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nLFhiZZKxD1z",
        "outputId": "34472912-28a0-41b9-cb2a-e24897169016"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Group Zero-result rate for Group (a) is : 5.652\n",
            "Group Zero-result rate for Group (b) is : 8.132\n"
          ]
        }
      ]
    }
  ]
}